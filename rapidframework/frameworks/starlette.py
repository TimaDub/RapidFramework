from .fastapi import FastapiManager


class StarletteManager(FastapiManager):
    def __init__(self, extra_libs = \
        ["sqlalchemy", "aiomysql", "python-multipart", "aiofiles"], **kwargs):
        
        self.extra_libs = extra_libs
        super().__init__(extra_libs, **kwargs)
