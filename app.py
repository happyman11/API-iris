#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:40:45 2021

@author: ravishekhartiwari
@website: https://www.rstiwari.com
"""
#%%
import pandas as pd
from flask import Flask, jsonify, request
import pickle5 as pickle
import json
import numpy as np
#%%


# load model
pickle_in = open('iris_model.pkl',"rb")
model = pickle.load(pickle_in)

app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])


def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
   


