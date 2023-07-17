import requests
import lxml.html as html
from util import send_msg
from conf import *
import re


def job():
    try:
        r = requests.get(checkHouseUrl)
        doc = html.fromstring(r.text)
        for el in doc.find_class("SearchResults-desktop"):
            content = el.text_content()
            if re.search(r"\d", content):
                print(content)
                send_msg("找到房子了" + content)
            else:
                print(content)
    except:
        pass
