import json
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

py_app = Flask(__name__)

@py_app.route("/api/")
def ping():
    return jsonify(
        error = "400",
        response = "Bad Request"
    )

# [GET] Fetch similiar words from dictionary
@py_app.route("/api/get_word=<string:word>", methods=['GET'])
def GetWord(word):
    return jsonify(
        response = word
    )

# [GET] Fetch all words from dictionary (without definition)
# This might be useful for NLP
@py_app.route("/api/get_allword", methods=['GET'])
def GetAllWord():
    return jsonify(
        response = word
    )

# [POST] Add a Word directly into the Database without any description
@py_app.route("/api/add_word=<string:word>", methods=['GET','POST'])
def AddWord(word):
    return jsonify(
        response = word
    )

# [POST] Add multiple words at once into the Database, json file needed
@py_app.route("/api/add_bulk", methods=['GET','POST'])
def AddBulk():
    if 'file' not in request.files:
        return jsonify(
            response = "False"
        )
    return jsonify(
        response = "True"
    )

@py_app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

if __name__=="__main__":
    py_app.run()