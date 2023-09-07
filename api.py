import pandas as pd
import flask
from flask import jsonify, request
import numpy as np
import os
import csv

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Read the CSV file and transform it to a list of dictionaries
gapminder = pd.read_csv("gapminder.csv").to_dict(orient='records')

@app.route('/', methods=['GET'])
def home():
    return "<h1>Greetings!</h1>"

@app.route('/gapminder/all', methods=['GET'])
def get_all_gapminder():
    return jsonify(gapminder)

@app.route('/gapminder', methods=['GET'])
def get_country_data():
    if 'country' in request.args:
        country = request.args['country']

        if any(row['country'] == country for row in gapminder):
            results = [elem for elem in gapminder if elem['country'] == country]
            return jsonify(results)
        else:
            return "Error: Please insert a valid country name."
    else:
        return "Error: No country provided. Please specify a country."

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0', debug=True)
