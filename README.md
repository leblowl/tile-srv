# tile-srv
Experimental Vector Tile Server

## Install
```shell
git clone https://github.com/leblowl/tile-srv && cd tile-srv
pip install --process-dependency-links .
```
## Dev
Launch app srv for dev
```shell
python setup.py dev
```

## Repl
Launch repl for dev
```shell
python setup.py repl
>>> import tile_srv.server as srv
>>> srv.up()
```
