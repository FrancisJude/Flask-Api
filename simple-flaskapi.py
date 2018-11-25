from flask import Flask, abort, jsonify, make_response, request
from flask_httpauth import HTTPBasicAuth
import os
auth = HTTPBasicAuth()
app = Flask(__name__)

@auth.get_password
def authorized(username):
    if username == os.environ.get("username"):
        return os.environ.get("password")
    return None

@auth.error_handler
def unauth():
    return make_response(jsonify({"error": "unauthorized request"}), 401)

@app.route('/<int:id>', methods = ["GET"])
def index(id):
    if id == 20:
        abort(404)
    return make_response(jsonify({"response": "success"}), 201)

@app.errorhandler(404)
def invalid(error):
    return make_response(jsonify({"error": "invalid url"}), 404)

@app.route('/add', methods = ["POST"])
@auth.login_required
def add():
    return jsonify(request.json), 201

if __name__ == '__main__':
    app.run(debug = True)
