########################################################################
# Main flask app for collecting requests and sending responses
########################################################################


from flask import Flask, jsonify, request
import json
from generator import generate


app = Flask(__name__)


@app.route("/api/<word1>/<word2>", methods=["GET"])
def api(word1: str, word2: str):
    if request.method == "GET":
        words = generate(word1, word2)
        
        if words:
            response, response_code = jsonify({"words": words}), 200
        else:
            response, response_code = jsonify("no words found"), 404
            
        return response, response_code
        
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)