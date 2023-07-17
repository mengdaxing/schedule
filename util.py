import requests
from conf import *


def send_msg(msg):
    r = requests.get(serverChan % (msg))
