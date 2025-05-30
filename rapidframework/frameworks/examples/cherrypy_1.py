import cherrypy

class HelloWorld:
    @cherrypy.expose
    def index(self):
        return "Hello, CherryPy!"

cherrypy.quickstart(HelloWorld())
