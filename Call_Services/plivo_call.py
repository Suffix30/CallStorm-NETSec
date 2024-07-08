import sys
import time
from plivo import RestClient
from config import plivo_config, voiceml, sourceNumbers

def callThem(toNumber, fromNumber, client):
    try:
        response = client.calls.create(
            from_=fromNumber,
            to=toNumber,
            answer_url=voiceml,
            answer_method='GET'
        )
        print(f"Plivo: Started call to {toNumber} from {fromNumber}")
    except Exception as err:
        print(f"Plivo: Error on {toNumber} from {fromNumber}: {err}")

if __name__ == "__main__":
    numToCall = sys.argv[1]
    client = RestClient(plivo_config['auth_id'], plivo_config['auth_token'])

    for sourceNumber in sourceNumbers:
        callThem(numToCall, sourceNumber, client)
        time.sleep(5)
