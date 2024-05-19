from flask import Flask, request, jsonify, send_from_directory, render_template, Response
from werkzeug.exceptions import Forbidden
from loguru import logger
from api.gpt_api import gpt
from flask_cors import CORS


logger.warning('[main] started...')


app = Flask(__name__, static_folder='static/', template_folder='static/')
app.debug = False
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

app.register_blueprint(gpt)
CORS(app)


def handle_error_request(error):
    logger.error(error)
    return error, error.code


app.register_error_handler(Forbidden, handle_error_request)


@app.route('/', methods=['GET', 'POST'])
def index():
    res_data = {
        'status': 'OK'
    }
    return jsonify(res_data)


if __name__ == "__main__":
    # Only for debugging while developing
    # app.logger.info('app instance path: {0}'.format(app.instance_path))
    # app.logger.info('app root path: {0}'.format(app.root_path))
    logger.info('[main] flask started', trace_id='t123')
    # worker = CommentReplyWorker()
    # worker.start()
    app.config['JSON_AS_ASCII'] = False
    app.run(host="0.0.0.0", debug=False, port=80, threaded=True)
