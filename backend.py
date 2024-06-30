from flask import Flask, render_template, request, jsonify
import requests
import json
from ast import literal_eval
  
app = Flask(__name__,template_folder="templates") 
  
@app.route("/") 
def hello(): 
    return render_template('frontend.html') 
  
@app.route('/process', methods=['POST']) 
def process(): 
    data = request.get_json() # retrieve the data sent from JavaScript 
    # process the data using Python code 
    print(data['value'])
    result = data['value']
    url = 'https://api.chaster.app/api/extensions/auth/sessions/'
    headers = {
        'Authorization': 'Bearer p4M6XodvwX7xO7dR1kDCJevM0cymOo9j'
    }
    response = requests.request("GET", url + data['value'], headers=headers)
    return response.text # return the result to JavaScript 

@app.route('/toggleFreeze', methods=['POST'])
def toggleFreeze():
    print("hello")
    url = 'https://api.chaster.app/api/extensions/session/'
    headers = {
        'Authorization': 'Bearer p4M6XodvwX7xO7dR1kDCJevM0cymOo9j'
    }
    data = {
        "name": "toggle_freeze"
    }
    sessionID = request.get_json()
    response = requests.post(url + sessionID + "/action", headers = headers, data = data)
    return response

if __name__ == '__main__': 
    app.run(debug=True) 
