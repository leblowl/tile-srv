import os
import tile_gen.app as app
from gevent import pywsgi

config_path = os.getcwd() + "/rsc/tilestache.cfg"

def application(env, start_response):
  if env['PATH_INFO'] == '/':
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello World!']
  else:
    start_response('404 Not Found', [('Content-Type', 'text/plain')])
    return ['Route not found.']

if __name__ == '__main__':
  print("tile-srv listening on 8088...")
  pywsgi.WSGIServer(('127.0.0.1', 8088), application).serve_forever()
