from flask import Flask, request
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from src.consts import HEADERS
from modules.helpers import *
import json

app = Flask(__name__, static_url_path='/', static_folder='./wolt-client/build')
limiter = Limiter(app, key_func=get_remote_address)
CORS(app)
start_scanning()

def add_headers(response):
    # add custom headers to the response
    response.headers = HEADERS

    # return the modified response object
    return response

# use the after_request decorator on the Flask instance
# to specify the function that should be called after every request
app.after_request(add_headers)


@app.route("/getUsersRequests", methods=["GET"])
@limiter.limit("5/minute")
def get_users_requests():
    if "email" in request.args:
        email = request.args.get("email")
        answer = get_urls_by_email(email)
        if answer is not None:
            return json.dumps({
                "pendingUrls": answer
            })
        else:
            return json.dumps({
                "status": "Please enter a valid email"
            }), 400

    return json.dumps({
        "status": "Error occur"
    }), 400


@app.route("/createRequestUrl", methods=["POST"])
@limiter.limit("5/minute")
def create_request_url():
    try:
        data = request.get_json()
        if data.get("email") and data.get("url"):
            email = data.get("email")
            url = data.get("url")
            answer = create_request_db(email, url)
            if answer:
                return json.dumps({
                    "isSuccess": True,
                    "message": "Successfully update to pending Urls"
                })
            else:
                return json.dumps({
                    "isSuccess": False,
                    "message": "Something went Wrong"
                }), 400

        return json.dumps({
            "status": "Error occur"
        }), 400
    except Exception as e:
        print(f"Unexpected error occured: {e}")
        return json.dumps({
            "status": "Error occur"
        }), 500


@app.route("/error", methods=["POST", "GET"])
@limiter.limit("5/minute")
def error():
    return json.dumps({
        "status": "Error occur"
        }), 400

if __name__ == '__main__':
    # start_scanning()
    app.run(debug=True, host="0.0.0.0", port=3333)
