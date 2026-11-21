from flask import Flask
app=Flask(__name__)

@app.route('/')
def Hello():
    return "<p>Hello from Shayan and Noman</p>"

@app.route('/')
def Hello1():
    return "<p>Hello from Noman</p>"

app.run(debug=True)