import json

from os import getenv

import requests

def lambda_handler(event, context):
    
    webhook_uri = getenv('Webhook_URI')
    message = json.dumps({'text': 'data'})
    response = requests.post(webhook_uri,data=message)
    
    return {
        'statusCode': response.status_code,
	'body': json.dumps(response.text)
    }
