import json
import ssl
import traceback

import requests
from flask_cors import CORS
from flask import Flask, request , make_response , jsonify , render_template
import yaml
from requests.adapters import HTTPAdapter
from urllib3 import PoolManager
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)

SWAGGER_URL = '/api'
API_URL = '/static/swagger-api.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "ref-seek"
    }
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

CORS(app)

configs = yaml.load(open('configs.yaml'), Loader=yaml.FullLoader)

refget_api_url = configs.get('refget_url')

class MyAdapter(HTTPAdapter) :
    def init_poolmanager(self, connections, maxsize, block=False, **kwargs):
        self.poolmanager = PoolManager(num_pools=connections ,
                                       maxsize=maxsize ,
                                       block=block ,
                                       ssl_version=ssl.PROTOCOL_SSLv23)


s = requests.Session()
s.mount('https://' , MyAdapter())


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/get_ref/<md5_checksum_id>", methods=['GET'])
def get_ref(md5_checksum_id):
    global id
    try:
        id = md5_checksum_id
        print(id)
        host = request.headers.get('Host') if request.headers.get('Host').split(":")[0] else "unknown"
        app.logger.info("New 'ref_get' request using id {} from host {}.".format(id, host))
        if not str(id.replace("\"", "").replace("'", "")):
            response = make_response(
                jsonify(
                    message = "Invalid MD5 sequence ID.",
                    status = "error"),
                400)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        url = refget_api_url.format(id)
        data = s.get(url)
        metadata = json.loads(data.content.decode("utf-8", "strict"))
        response = make_response(
            jsonify(
                message ="Returning sequence metadata.",
                status= "success",
                data = metadata),
            200)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = make_response(
            jsonify(
                message="Something went wrong. Please try again later.",
                status = "error",
                data=None),
            500, None)
        response.headers.add('Access-Control-Allow-Origin', '*')
        app.logger.error("Error while processing 'get_ref' request using id {}.\nError:  {}"
                         .format((id), traceback.print_exc(e)))
        return response


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)