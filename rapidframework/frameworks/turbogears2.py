from ..template import Template


class TurboGears2Manager(Template):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def install_framework(self, **kwargs):
        return super().install_framework(libs=\
            ["sqlalchemy", "alembic", "tgext.auth", "tgext.admin"], **kwargs)
