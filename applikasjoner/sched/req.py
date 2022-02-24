import requests
import json
import os
from time import sleep 

TID = os.environ['TID_MELLOM_FORESPORSLER']
HOST = os.environ['DJANGO_HOST_PORT']

url = f"http://{HOST}/api?int={TID}"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 'Content-type': 'application/json', 'Accept': 'text/plain'}


while True:
    r = requests.get(url, headers=headers)
    sleep(int(TID))

