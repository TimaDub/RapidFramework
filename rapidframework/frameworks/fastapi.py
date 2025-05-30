from ..template import Template

class FastapiManager(Template):
    extra_libs = ["sqlalchemy", "python-multipart", "databases", "python-multipart", "aiofiles", "uvicorn", "jinja2", "bcrypt"]
    extra_dirs = ["db"]
    
class StarletteManager(FastapiManager):
    extra_libs = ["aiomysql"]
    
class LitestarManager(StarletteManager):
    extra_libs = ["msgspec", "starlette", "httpx"]
