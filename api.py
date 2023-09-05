import pandas as pd
from flask import jsonify, request
import numpy as np
import flask
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

gapminder = pd.read_csv("gapminder.csv")
gapminder_list = []
nrows = gapminder.shape[0]
for i in range(nrows):
    ser = gapminder.loc[i, :]
    row_dict = {}
    for idx, val in zip(ser.index, ser.values):
        if type(val) is str:
            row_dict[idx] = val
        elif type(val) is np.int64:
            row_dict[idx] = int(val)
        elif type(val) is np.float64:
            row_dict[idx] = float(val)
    gapminder_list.append(row_dict)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

@app.route('/gapminder/all', methods=['GET'])
def gapminder_all():
    return jsonify(gapminder_list)

@app.route('/gapminder', methods=['GET'])
def gapminder():
    if 'country' in request.args:
        country = request.args['country']
    else:
        return "Error: No country provided. Please specify a country." 
    results = []
    for elem in gapminder_list:
        if elem['country'] == country:
            results.append(elem)

    return jsonify(results)

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)

