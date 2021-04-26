from flask import Flask
import os
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    message = f'Hello from Wenqian, now is {now}!'
    return message


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)

