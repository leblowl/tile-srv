from setuptools import setup

setup(name = 'tile-srv',
      version = '0.1.0',
      classifiers = ['Programming Language :: Python :: 2.7'],
      install_requires = ['Cython==0.22.1',
                          'gevent==1.1b2.dev0',
                          'greenlet==0.4.7',
                          'wheel==0.24.0',
                          'tile-gen==0.1.0'])
