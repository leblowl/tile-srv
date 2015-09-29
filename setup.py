from setuptools import Command, setup
import sys, os, os.path as path, code

env = {'source_paths': ['src', 'rsc', '../tile-gen/src']}

def init_env(env):
  for path in env.get('source_paths'):
    sys.path.append(os.path.abspath(path))

class Dev(Command):
  description = "Launch app srv for dev"
  user_options = []

  def initialize_options(self):
    pass

  def finalize_options(self):
    pass

  def run(self):
    import tile_srv.server as srv; srv.up()

class Repl(Command):
  description = "Launch repl for dev"
  user_options = []

  def initialize_options(self):
    pass

  def finalize_options(self):
    pass

  def run(self):
    code.interact(local=globals())

init_env(env)
setup(name = 'tile-srv',
      version = '0.1.0',
      classifiers = ['Programming Language :: Python :: 2.7'],
      dependency_links = ['git+https://github.com/leblowl/tile-gen#egg=tile-gen-0.1.0'],
      install_requires = ['Cython==0.22.1',
                          'bottle==0.12.8',
                          'gevent==1.1b1',
                          'greenlet==0.4.7',
                          'Jinja2==2.8',
                          'tile-gen==0.1.0',
                          'wheel==0.24.0'],
      cmdclass = {"dev":  Dev,
                  "repl": Repl})
