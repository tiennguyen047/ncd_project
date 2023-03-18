from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def hello():
    print("test code")
    print("test code")
    return 'Hello World NQT'

if __name__ == "__main__":
    print("deployment NCD service with port {}".format(os.environ['PORT']))
    app.run(host="0.0.0.0", port=os.environ['PORT'])