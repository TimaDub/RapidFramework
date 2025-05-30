import grok

class Hello(grok.View):
    def render(self):
        return "Hello, Grok!"

class MyApp(grok.Application, grok.Container):
    pass
