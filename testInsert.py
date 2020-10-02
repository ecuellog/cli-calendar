import boto3

def addEvent(name, calendar, description,  start, end):
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    
    events = dynamodb.Table('events')
    response = events.put_item(
        Item={
            'name': name,
            'calendar': calendar,
            'description': description,
            'start': start,
            'end': end
        }
    )

    return response

if __name__ == '__main__':
    event_resp = addEvent('Chat with Ed', 'Personal', 'Chat with ed about blah blah', '2020-10-01T03:21:59+00:00', '2020-10-01T01:21:59+00:00')
    print('success')
    pprint(event_resp, sort_dicts=False)

