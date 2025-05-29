from .fastapi import FastapiManager


class TornadoManager(FastapiManager):
    def __init__(self, extra_libs = \
        ["motor", "aiomysql", "pytest-tornado", "aiofiles"], **kwargs):
        super().__init__(extra_libs, **kwargs)
