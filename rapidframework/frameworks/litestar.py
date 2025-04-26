from .starlette import StarletteManager

class LitestarManager(StarletteManager):
    def __init__(self, framework_name="litestar", extra_libs=None, **kwargs):
        extra_libs = (extra_libs or []) + ["msgspec", "starlette", "httpx"]
        super().__init__(framework_name, extra_libs=extra_libs, **kwargs)