from ..template import Template

class PyramidManager(Template):
    extra_libs = ["sqlalchemy", "alembic", "pyramid_tm", "pyramid_jinja2", "pyramid_authsanity"]
    
class TornadoManager(Template):
    extra_libs = ["motor", "aiomysql", "pytest-tornado", "aiofiles"]
    
class Web2pyManager(Template): ...

class GrokManager(Template):
    extra_libs = ["z3c.sqlalchemy", "zope.sqlalchemy", "alembic"]
    
class FlaskManager(Template):
    extra_libs = ["flask_sqlalchemy", "flask_migrate", "flask_wtf", "flask_login"]
    extra_dirs = ["db"]
    
class CherryPyManager(Template):
    extra_libs = ["sqlalchemy", "alembic", "Jinja2", "authlib"]
    
class BottleManager(Template):
    extra_libs = ["sqlalchemy", "bottle-sqlalchemy", "alembic", "bottle-login", "wtforms"]
    extra_libs = ["db"]
    
class SocketifyManager(Template):
    extra_libs = ["ormar", "databases", "pydantic", "jinja2", "authlib"]
    
class TurboGears2Manager(Template):
    extra_libs = ["sqlalchemy", "alembic", "tgext.auth", "tgext.admin"]