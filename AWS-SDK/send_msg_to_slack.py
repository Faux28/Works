import requests

message = '{"text":"message sent to slack"}'
response = requests.post('https://hooks.slack.com/services/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',data=message)

print(response.text)
