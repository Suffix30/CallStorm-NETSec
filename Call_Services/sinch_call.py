import sys
import time
import requests
from config import sinch_config, voiceml, sourceNumbers
import base64

def callThem(toNumber, fromNumber):
    url = "https://calling.api.sinch.com/calling/v1/callouts"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {base64.b64encode(f'{sinch_config['app_key']}:{sinch_config['app_secret']}'.encode()).decode()}"
    }
    data = {
        "method": "ttsCallout",
        "ttsCallout": {
            "cli": fromNumber,
            "destination": {"type": "number", "endpoint": toNumber},
            "domain": "pstn",
            "custom": "MyCustomData",
            "locale": "en-US",
            "prompts": [
                {
                    "type": "file",
                    "file": voiceml
                }
            ]
        }
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 201:
            print(f"Sinch: Started call to {toNumber} from {fromNumber}")
        else:
            print(f"Sinch: Error {response.status_code} - {response.text}")
    except Exception as err:
        print(f"Sinch: Error on {toNumber} from {fromNumber}: {err}")

if __name__ == "__main__":
    numToCall = sys.argv[1]

    for sourceNumber in sourceNumbers:
        callThem(numToCall, sourceNumber)
        time.sleep(5)
