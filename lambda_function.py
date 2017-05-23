import requests
import os

def lambda_handler(event, context):
    req = requests.post(
        'https://www.beeminder.com/api/v1/users/me/goals/{}/datapoints.json'.format(os.getenv('BEEMINDER_GOAL')),
        json={
            'auth_token': os.getenv('BEEMINDER_AUTH_TOKEN'),
            'value': 1,
            'comment': 'submitted via aws iot button, woo'
        }
    )
    print(req.status_code)
    return req.status_code
