from ..template import Template


class CherryPyManager(Template):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def install_framework(self, **kwargs):
        return super().install_framework(libs=\
            ["sqlalchemy", "alembic", "Jinja2", "authlib"], **kwargs)
