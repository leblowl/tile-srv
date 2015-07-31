import os
import sys
import tile_gen.app as tile_gen
from gevent import pywsgi
from bottle import Bottle, response

sys.path.append(os.getcwd() + '/rsc')

def get_tile(layer, z, x, y, ext):
  mimetype, body = tile_gen.get_tile(layer, z, x, y, ext)
  response.headers['Access-Control-Allow-Origin'] = '*'
  response.headers['Content-Type'] = mimetype
  return body

app = Bottle()
app.route('/<layer>/<z:int>/<x:int>/<y:int>.<ext>', 'GET', get_tile)
app.error(404)(lambda err : 'Not found.')

if __name__ == '__main__':
  print("tile-srv listening on 8088...")
  pywsgi.WSGIServer(('127.0.0.1', 8088), app).serve_forever()
