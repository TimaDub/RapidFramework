from ..template import Template


class FlaskManager(Template):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def install_framework(self, **kwargs):
        return super().install_framework(libs=\
            ["flask_sqlalchemy", "flask_migrate", "flask_wtf", "flask_login"], **kwargs)
