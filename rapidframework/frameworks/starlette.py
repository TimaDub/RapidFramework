from .fastapi import FastapiManager


class StarletteManager(FastapiManager):
    def __init__(self, framework_name="starlette", extra_libs = \
        ["sqlalchemy", "aiomysql", "python-multipart", "aiofiles"], **kwargs):
        
        self.extra_libs = extra_libs
        super().__init__(framework_name, extra_libs, **kwargs)
