import json
from os import getenv

import requests

def lambda_handler(event, context):
    
    webhook_url = getenv('Webhook_URL')
    message = '{"text":"Hello"}'
    response = requests.post(webhook_url,data=message)
    
    return {
        'statusCode': response.status_code,
    }
