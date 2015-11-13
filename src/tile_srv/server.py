import os
import sys
import tile_gen.core as tile_gen
from tile_srv.config import config
from gevent import pywsgi
from bottle import Bottle, response

def get_tile(layer, z, x, y, ext):
  mimetype, body = tile_gen.get_tile(layer, z, x, y, ext)
  response.headers['Access-Control-Allow-Origin'] = '*'
  response.headers['Content-Type'] = mimetype
  return body

def up (host='127.0.0.1', port=8088):
  print('tile-srv listening on ' + host + ':' + str(port) + '...')
  pywsgi.WSGIServer((host, port), app).serve_forever()

app = Bottle()
app.route('/<layer>/<z:int>/<x:int>/<y:int>.<ext>', 'GET', get_tile)
app.error(404)(lambda err : 'Not found.')
tile_gen.init_env(config)

if __name__ == '__main__':
  up()
