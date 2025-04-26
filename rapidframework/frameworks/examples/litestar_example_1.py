from litestar import Litestar, get

@get("/")
async def hello_world() -> dict[str, str]:
    """Keeping the tradition alive with hello world."""
    return {"hello": "world"}

app = Litestar(route_handlers=[hello_world])