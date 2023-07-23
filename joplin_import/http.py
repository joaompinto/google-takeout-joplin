import requests
import urllib
import json
from os import environ


URL="http://localhost:41184/"
TOKEN=environ['JOPLIN_TOKEN']

def post(url, payload):
    """POST request to url"""
    url = URL + urllib.parse.quote(url)
    reply = requests.post(f"{url}?token={TOKEN}", data=json.dumps(payload))
    reply.raise_for_status()
    return reply.json()