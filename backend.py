from flask import Flask, render_template, request
import requests
import json
import websockets
import asyncio
import threading
from client import Client, ClientConfig, GameConfig
  
app = Flask(__name__,template_folder='templates') 
headers = { 'Authorization': 'Bearer <AUTH TOKEN>' }
  
@app.route('/') 
def init(): 
    return render_template('frontend.html') 

def getSessionURL(mainToken):
    # sets the url for the GET request
    url = 'https://api.chaster.app/api/extensions/auth/sessions/'

    # makes the GET request to the Chaster API
    response = requests.request('GET', url + mainToken, headers=headers)

    # converts the response to a json object
    json_obj = json.loads(response.text)

    # parses the session object to get the sessionID
    sessionID = str(json_obj['session']['sessionId']) 

    # sets the url for the POST request
    return 'https://api.chaster.app/api/extensions/sessions/' + sessionID + '/action'

def connect_websocket(serverPort, playerName, serverPassword):
    client = Client(ClientConfig(serverPort, playerName, serverPassword), GameConfig("Factorio"))
    task = asyncio.run(client.run())

@app.route('/establishConnection', methods=['POST'])
def establishConnection():
    # establishes the connection to the Archipelago server
    connect_websocket(
        request.form['serverPort'],     # receives server URL from form 
        request.form['playerName'],     # receives player name from form
        request.form['serverPassword']) # receives server password from form

    # immediately freezes the lock upon loading the Archip
    url = getSessionURL(request.form['value'])
    data = {
    'action': {
        'name': 'freeze'
        }
    }

    # makes the POST request to the Chaster API
    response = requests.post(url, headers = headers, json = data)
    print(response.text)
    return mainToken

def freezePlayer():
    # immediately freezes the lock upon loading the Archip
    url = getSessionURL(request.form['value'])
    data = {
    'action': {
        'name': 'freeze'
        }
    }

    # makes the POST request to the Chaster API
    response = requests.post(url, headers = headers, json = data)
    print(response.text)

@app.route('/processAPItemGet', methods=['POST'])
def processAPItemGet():
    # sets the url for the POST request
    url = getSessionURL(request.form['value'])

    item = 'addTimeTrap'

    # resolves the item received by Archipelago
    match item:
        case 'addTimeTrap':
            data = {
            'action': {
                'name': 'add_time',
                'params': 3600
                }
            }

        case 'pilloryTrap':
            data = {
            'action': {
                'name': 'pillory',
                'params': {
                    'duration': 3600,
                    'reason': 'I suck at video games!'
                    }
                }
            }

        case 'unfreezeVictory':
            data = {
            'action': {
                'name': 'unfreeze'
                }
            }

    response = requests.post(url, headers = headers, json = data)
    print(response.text)
    return mainToken

if __name__ == '__main__': 
    app.run(debug=True) 
