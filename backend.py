from flask import Flask, render_template, request
import requests
import json
import socket
  
app = Flask(__name__,template_folder="templates") 
  
@app.route("/") 
def init(): 
    return render_template('frontend.html') 

@app.route('/toggleFreeze', methods=['POST'])
def toggleFreeze():
    # receives the main token from the front end
    mainToken = request.form['value']
    print(request.form['serverIP'])
    print(request.form['serverPort'])
    print(request.form['serverPassword'])
    print(request.form['playerName'])

    # sets the url for the GET request
    url = 'https://api.chaster.app/api/extensions/auth/sessions/'
    headers = {
        'Authorization': 'Bearer p4M6XodvwX7xO7dR1kDCJevM0cymOo9j'
    }

    # makes the GET request to the Chaster API
    response = requests.request("GET", url + mainToken, headers=headers)

    # converts the response to a json object
    json_obj = json.loads(response.text)

    # parses the session object to get the sessionID
    sessionID = str(json_obj["session"]["sessionId"]) 

    # sets the url for the POST request
    url = 'https://api.chaster.app/api/extensions/sessions/' + sessionID + '/action'
    data = {
    "action": {
        "name": "freeze"
        }
    }

    # makes the POST request to the Chaster API
    response = requests.post(url, headers = headers, json = data)
    print(response.text)
    return mainToken

if __name__ == '__main__': 
    app.run(debug=True) 
