from ..template import Template


class FastapiManager(Template):
    def __init__(self, extra_libs: list = \
        ["sqlalchemy", "databases", "python-multipart", "aiofiles"], **kwargs):
        
        self.extra_libs = extra_libs
        super().__init__(**kwargs)

    def setup_framework(self, extra_dirs=["db"]):
        return super().setup_framework(extra_dirs=extra_dirs)
    
    def install_framework(self, **kwargs):
        self.extra_libs.extend(["uvicorn", "jinja2", "bcrypt"])
        return super().install_framework(libs=\
            self.extra_libs, **kwargs)
