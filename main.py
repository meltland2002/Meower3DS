# using flask_restful
import flask
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import websocket
import time
import threading
import json

user = "USERNAME" # set this to your Meower username
pswd = "PASSWORD" # set this to your Meower password
hostip = "192.168.1.xxx" # set this to your computer's ip

app = Flask(__name__)
api = Api(app)

queue = []

def on_open(wsapp):
  wsapp.send('{"cmd": "direct", "val": "meower"}')
  time.sleep(1)
  wsapp.send('{"cmd": "direct", "val": {"cmd": "authpswd", "val": {"username": "' + user + '", "pswd": "' + pswd + '"}}}')

def on_message(ws, message):
  queue.append(json.loads(message))

wsapp = websocket.WebSocketApp("wss://server.meower.org/", on_open=on_open, on_message=on_message)

class Main(Resource):
  def get(self):
    resp = flask.Response("OK")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

class Post(Resource):
  def get(self, msg):
    wsapp.send('{"cmd": "direct", "val": {"cmd": "post_home", "val": "' + msg + '"}}')
    resp = flask.Response("OK")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

class Queue(Resource):
  def get(self):
    global queue
    p = json.dumps(queue)
    queue = []
    resp = flask.Response(str(p))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

api.add_resource(Main, '/')
api.add_resource(Post, '/post/<string:msg>')
api.add_resource(Queue, '/queue')

def runitforever():
  wsapp.run_forever(reconnect=1)
  
# driver function
if __name__ == '__main__':
  x = threading.Thread(target=runitforever, daemon=True)
  x.start()
  app.run(host=hostip, port=5000, debug=True, threaded=True)