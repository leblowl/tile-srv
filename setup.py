from setuptools import setup

setup(name = 'tile-srv',
      version = '0.1.0',
      classifiers = ['Programming Language :: Python :: 2.7'],
      dependency_links = ['git+https://github.com/leblowl/tile-gen#egg=tile-gen-0.1.0'],
      install_requires = ['Cython==0.22.1',
                          'bottle==0.12.8',
                          'gevent==1.1b1',
                          'greenlet==0.4.7',
                          'tile-gen==0.1.0',
                          'wheel==0.24.0'])
