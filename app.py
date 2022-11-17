from starlite import Starlite

from routes import hello

app = Starlite(route_handlers=[hello])
