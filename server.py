from flask import Flask, request
import json


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        pass
    else:
        #Find the user from the given details.
        attrs = request.get_json()
        return attrs, 200



if __name__ == "__main__":
    app.run()