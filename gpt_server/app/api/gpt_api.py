from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest
from models.gpt_service import GPTService
import json


gpt = Blueprint('gpt', __name__, url_prefix='/gpt')


@gpt.route('/', methods=['GET', 'POST'])
def index():
    res_data = {
        'status': 'GPT OK'
    }
    return jsonify(res_data)


@gpt.route('/generate', methods=('POST',))
def generate():
    data = request.json
    messages = data.get('messages', None)
    max_tokens = data.get('max_tokens', None)
    stop_words = data.get('stop_words', None)
    if not messages or not max_tokens:
        raise BadRequest(
            'following parameters are required: messages, max_tokens')
    result = GPTService.generate_text(messages, max_tokens, stop_words)
    return jsonify(
        {
            'status': 'OK',
            'candidates': result
        }
    )


if __name__ == '__main__':
    pass