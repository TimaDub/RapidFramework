from socketify import App

app = App()

@app.get("/")
def hello(res, req):
    res.end("Hello, Socketify!")

app.listen(3000, lambda config: print("Listening on port 3000"))
app.run()
