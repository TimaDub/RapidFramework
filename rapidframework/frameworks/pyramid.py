from ..template import Template


class PyramidManager(Template):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def install_framework(self, **kwargs):
        return super().install_framework(libs=\
            ["sqlalchemy", "alembic", "pyramid_tm", "pyramid_jinja2", "pyramid_authsanity"], **kwargs)

