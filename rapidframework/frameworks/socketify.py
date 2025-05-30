from ..template import Template


class SocketifyManager(Template):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def install_framework(self, **kwargs):
        return super().install_framework(libs=\
            ["ormar", "databases", "pydantic", "jinja2", "authlib"], **kwargs)
 
