import os
import sys
import tile_gen.app as tg
from gevent import pywsgi
from bottle import Bottle, Response

sys.path.append(os.getcwd() + '/rsc')

def get_tile(layer, z, x, y, ext):
  mimetype, body = tg.get_tile(layer, z, x, y, ext)
  return Response(body, 200, {content-type: mimetype})

app = Bottle()
app.route('/<layer>/<z:int>/<x:int>/<y:int>.<ext>', 'GET', get_tile)
app.error(404)(lambda err : 'Not found.')

if __name__ == '__main__':
  print("tile-srv listening on 8088...")
  pywsgi.WSGIServer(('127.0.0.1', 8088), app).serve_forever()
