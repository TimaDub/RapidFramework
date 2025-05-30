from ..template import Template


class BottleManager(Template):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def install_framework(self, **kwargs):
        return super().install_framework(libs=\
            ["sqlalchemy", "bottle-sqlalchemy", "alembic", "bottle-login", "wtforms"], **kwargs)
