import os
import requests

HOST = os.environ.get('HOST')


def check():
    response = requests.get(str(HOST) + '/api/check/')
    discords = list(response.content.decode('UTF-8').split('#$#'))
    return discords
