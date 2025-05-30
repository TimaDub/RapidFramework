from bottle import route, run

@route('/')
def hello():
    return "Hello, Bottle!"

run(host='localhost', port=8080)
