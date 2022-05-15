import json
import urllib3
import boto3

def lambda_handler(event, context):
    htttp = urllib3.PoolManager()
    s3 = boto3. client("s3")
    if event:
        file_obj = event["Records"][0]
        bucketname=str(file_obj['s3']['bucket']['name'])
        
        filename = str(file_obj['s3']['object ']['key'])

        print("Filename:", filename)
        file0bj=s3.get_object(Bucket-bucketname,Key=filename)
        
        file_content = file0bj["Body"].read().decode('utf-8')
            
       # data = {"texts": "Sample message from lambda function"}
        data = {"texts": file_content}
         
        r = htttp.request("POST",
                          "https://hooks.slack.com/services/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",
                          body = json.dumps(data), 
                          headers = {"Content-Type": "application/json"})
        # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
