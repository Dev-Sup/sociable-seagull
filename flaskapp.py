import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory
import requests


app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

@app.route('/page')
def page():
    url = 'https://oauth.vk.com/authorize'
    client_id = '5861520'
    scope = '1311746'
    
    payload = {
        'client_id' : client_id,
        'redirect_uri' : 'http://sociableseagull-devsup.rhcloud.com/oauth',
        'display' : 'popup',
        'scope' : scope,
        'response_type' : 'code',
        'v' : '5.62',
    }
    
    data = requests.get(url, params = payload).content
    return data
    #return "It works!"
    
@app.route('/oauth')
def oauth() :
    return '1'

if __name__ == '__main__':
    app.run()
