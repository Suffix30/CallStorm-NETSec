import sys
import time
import vonage
from config import nexmo_config, voiceml, sourceNumbers

def callThem(toNumber, fromNumber, client):
    try:
        response = client.voice.create_call({
            'to': [{'type': 'phone', 'number': toNumber}],
            'from': {'type': 'phone', 'number': fromNumber},
            'answer_url': [voiceml]
        })
        print(f"Nexmo: Started call to {toNumber} from {fromNumber}")
    except Exception as err:
        print(f"Nexmo: Error on {toNumber} from {fromNumber}: {err}")

if __name__ == "__main__":
    numToCall = sys.argv[1]
    client = vonage.Client(key=nexmo_config['api_key'], secret=nexmo_config['api_secret'])
    voice = vonage.Voice(client)

    for sourceNumber in sourceNumbers:
        callThem(numToCall, sourceNumber, voice)
        time.sleep(5)
