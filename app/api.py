import os
import logging
import flask
from urllib.parse import urlparse
from flask import send_file
from flask import request
from flask import abort
from flask import jsonify
from flask import make_response

app = flask.Flask(__name__)
app.config["DEBUG"] = True
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
log = logging.getLogger(__name__)

def pulloutpath(parsed):

    try:
        path = parsed.path
        resourcepath = '../resources' + path
        log.info(path)
        log.info(resourcepath)
        return(resourcepath)
    except Exception as e:
        abort(500)
        return

@app.route('/', methods=['GET', 'HEAD'])
def home():

    # curl -v http://127.0.0.1:5000

    log.info('Service Index')
    log.info('GET, HEAD')

    # urlparse method returns the following:
    # ParseResult(scheme='http', netloc='127.0.0.1:5000', path='/', params='', query='', fragment='')

    parsed = urlparse(request.url)
    resourcepath = pulloutpath(parsed)
    resourcepath += 'index.json'
    log.info(resourcepath)

    try:
        return send_file(resourcepath)
    except FileNotFoundError:
        abort(404)
        return
    except Exception as e:
        abort(500)
        return

@app.route('/<string:collection>', methods=['GET', 'HEAD', 'POST'])
def bars(collection):

    # ToDo: Have this handle the /bars/ path as well.

    log.info('Collection')

    if request.method in ['GET', 'HEAD']:

        # curl -v http://127.0.0.1:5000/bars

        log.info('GET, HEAD')
        parsed = urlparse(request.url)
        resourcepath = pulloutpath(parsed)
        resourcepath += '/index.json'

        try:
            return send_file(resourcepath)
        except FileNotFoundError:
            abort(404)
            return
        except Exception as e:
            abort(500)
            return

    elif request.method in ['POST']:

        # curl -v --data "temp" http://127.0.0.1:5000/bars

        # In rough order of operations...
        # ToDo: Check the content-type header = application/json.
        # ToDo: Validate the incoming data against the schema referenced in the data.
        # ToDo: Add the hypermedia operations.
        # ToDo: Write the new resource.
        # ToDo: Respond with 201 Created status header.
        # ToDo: Respond with the Location header (full URI).
        # ToDo: Respond with the ETag header.
        # ToDo: Respond with the resource representation in the payload.

        log.info('POST')

        abort(501)

        return

@app.route('/<string:collection>/<string:id>', methods=['GET', 'HEAD', 'PUT'])
def barsindividual(collection,id):

    log.info('Individual Resource:' + collection + '/' + id)

    if request.method in ['GET', 'HEAD']:

        # curl -v http://127.0.0.1:5000/bars/0b913d0f-062f-4167-a672-bbe52a73259b.json

        log.info('GET, HEAD')
        parsed = urlparse(request.url)
        resourcepath = pulloutpath(parsed)

        try:
            return send_file(resourcepath)
        except FileNotFoundError:
            abort(404)
            return
        except Exception as e:
            abort(500)
            return

    elif request.method in ['PUT']:

        # curl -v -X PUT --data "temp" http://127.0.0.1:5000/bars/0b913d0f-062f-4167-a672-bbe52a73259b.json

        # In rough order of operations...
        # ToDo: Check the content-type header = application/json.
        # ToDo: Check the incoming If-Match value against the current ETag -- reject request if it doesn't match.
        # ToDo: Validate the incoming data against the schema referenced in the data -- reject request if not valid.
        # ToDo: Create a copy of the existing resource with new UUID.
        # ToDo: Add the URI to the history array of the resource.
        # ToDo: Modify the hypermedia operations, if necessary.
        # ToDo: Write the new resource.
        # ToDo: Respond with the ETag header.
        # ToDo: Respond with 200 OK.
        # ToDo: Respond with the resource representation in the payload.

        log.info('PUT')

        abort(501)

        return

@app.after_request
def add_header(response):

    response.headers["Cache-Control"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers["Content-Type"] = "application/json"
    return response

@app.errorhandler(400)
def not_implemented_400(e):

    response = make_response(jsonify({"error": "collection"}), 400)
    log.debug(e)
    return response

@app.errorhandler(404)
def not_implemented_404(e):

    response = make_response(jsonify({}), 404)
    log.debug(e)
    return response

@app.errorhandler(500)
def not_implemented_500(e):

    response = make_response(jsonify({}), 500)
    log.debug(e)
    return response

@app.errorhandler(501)
def not_implemented_501(e):

    response = make_response(jsonify({}), 501)
    log.debug(e)
    return response

app.run()
