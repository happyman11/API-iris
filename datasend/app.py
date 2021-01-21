#import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template

import requests
import json
import os

url=' https://apiirisflower.herokuapp.com/'

data = {'A': 5,
       'b': 1,
       'c': 3,
       'd': 4}
data = json.dumps(data)
send_requests=requests.post(url,data)
print(send_requests)
result=send_requests.json()
#result=json.loads(result)
labels = ['setosa', 'versicolor', 'virginica']
print(labels[result['results']['results']])





