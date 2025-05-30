from ..template import Template


class GrokManager(Template):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def install_framework(self, **kwargs):
        return super().install_framework(libs=\
            ["z3c.sqlalchemy", "zope.sqlalchemy", "alembic"], **kwargs)

