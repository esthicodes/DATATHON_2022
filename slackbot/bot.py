from flask import Flask, Response
from slackeventsapi import SlackEventAdapter
import os
from threading import Thread
from slack import WebClient
from qa_pipeline import generate_answer
from qa_model import call_gpt3 #, setup_responder# call_hs
from qa_model_v2 import call_hs, setup_responder


from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.


# This `app` represents your existing Flask app
app = Flask(__name__)

greetings = ["hi", "hello", "hello there", "hey"]

SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
slack_token = os.environ.get("slack_token")
VERIFICATION_TOKEN = os.environ.get("VERIFICATION_TOKEN")
print(slack_token)
print(VERIFICATION_TOKEN)
print(SLACK_SIGNING_SECRET)
#instantiating slack client
slack_client = WebClient(slack_token)

responder = setup_responder()

# An example of one of your Flask app's routes
@app.route("/")
def event_hook(request):
    json_dict = json.loads(request.body.decode("utf-8"))
    if json_dict["token"] != VERIFICATION_TOKEN:
        return {"status": 403}

    if "type" in json_dict:
        if json_dict["type"] == "url_verification":
            response_dict = {"challenge": json_dict["challenge"]}
            return response_dict
    return {"status": 500}
    return


slack_events_adapter = SlackEventAdapter(
    SLACK_SIGNING_SECRET, "/slack/events", app
)  


@slack_events_adapter.on("app_mention")
def handle_message(event_data):
    def send_reply(value):
        event_data = value
        message = event_data["event"]
        if message.get("subtype") is None:
            question = message.get("text")
            channel_id = message["channel"]
            # message = call_gpt3(responder, question)
            message = call_hs(question)
            # message = message + "\n" + message_hs

            slack_client.chat_postMessage(channel=channel_id, text=message)
    thread = Thread(target=send_reply, kwargs={"value": event_data})
    thread.start()
    return Response(status=200)


# Start the server on port 3000
if __name__ == "__main__":
  app.run(port=3000)