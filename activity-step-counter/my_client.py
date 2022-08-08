
import requests
import json


"""
put data on server
"""


def put_activity(data):
    url = 'http://10.201.60.55:5000/act/' + str(data)
    r = requests.put(url)
    # count_call()
    json_data = json.loads(r.text)
    # print(json_data)
    # return int(json_data["result"])
