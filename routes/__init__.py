from starlite import get, MediaType

@get("/{name:str}", media_type=MediaType.TEXT)
def hello(name: str) -> str:
    return "Hello " + name
