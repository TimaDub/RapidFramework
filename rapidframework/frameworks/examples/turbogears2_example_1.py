from tg import expose, TGController, AppConfig
from wsgiref.simple_server import make_server

class RootController(TGController):
    @expose()
    def index(self):
        return "Hello, TurboGears!"

config = AppConfig(minimal=True, root_controller=RootController())
application = config.make_wsgi_app()

if __name__ == "__main__":
    print("Serving on http://localhost:8080")
    make_server('', 8080, application).serve_forever()
