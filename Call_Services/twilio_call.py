import sys
import time
from twilio.rest import Client
from config import twilio_config, voiceml, sourceNumbers

def callThem(toNumber, fromNumber, client):
    try:
        call = client.calls.create(
            to=toNumber,
            from_=fromNumber,
            record=True,
            url=voiceml,
            method="GET",
        )
        print(f"Twilio: Started call to {toNumber} from {fromNumber}")
    except Exception as err:
        print(f"Twilio: Error on {toNumber} from {fromNumber}: {err}")

if __name__ == "__main__":
    numToCall = sys.argv[1]
    client = Client(twilio_config['account_sid'], twilio_config['auth_token'])

    for sourceNumber in sourceNumbers:
        callThem(numToCall, sourceNumber, client)
        time.sleep(5)
