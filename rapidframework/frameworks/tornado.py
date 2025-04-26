from .fastapi import FastapiManager


class TornadoManager(FastapiManager):
    def __init__(self, framework_name="tornado", extra_libs = \
        ["motor", "aiomysql", "pytest-tornado", "aiofiles"], **kwargs):
        super().__init__(framework_name, extra_libs, **kwargs)
