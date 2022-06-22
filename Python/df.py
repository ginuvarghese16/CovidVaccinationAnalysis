# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:20:21 2021

@author: Ginu
"""
import flask
from flask import request, jsonify
import pandas as pd
app = flask.Flask(__name__)
app.config["DEBUG"] = True
pl = pd.read_csv(r'C:\Users\Chikku\OneDrive - Dundalk Institute of Technology\Documents\Spyder\country_vaccinations_v1.1.csv')

@app.route('/', methods=['GET'])
def home():
    return 'COVID VACCINATION API'


@app.route('/api/v1/COVID19/vaccinations/all', methods=['GET'])
def api_all():
    result = {}
    for index, row in pl.iterrows():
        result[index] = dict(row)
        list1=[result]
    return jsonify(list1)

@app.route('/api/v1/COVID19/vaccinations', methods=['GET'])
def api_country():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
       
    
    if 'country' in request.args:
        country = [request.args.get('country')]
        list2=[]
        sel_data =  pl[pl["country"].isin(country)]
        results3 = {}
        for index, row in sel_data.iterrows():
            results3[index] = dict(row)
            list2=[results3]
    elif 'continent' in request.args:
        continent = [request.args.get('continent')]
        list2=[]   
        sel_data =  pl[pl["continent"].isin(continent)]
        results3 = {}
        for index, row in sel_data.iterrows():
            results3[index] = dict(row)
            list2=[results3]
    elif 'iso_code' in request.args:
        iso_code = [request.args.get('iso_code')]
        list2=[]   
        sel_data =  pl[pl["iso_code"].isin(iso_code)]
        results3 = {}
        for index, row in sel_data.iterrows():
            results3[index] = dict(row)
            list2=[results3]
    else:
        return "Error: No field provided. Please specify."
    
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(list2)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
app.run()

