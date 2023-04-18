from flask import Blueprint, jsonify, request
import os

gpt_routes = Blueprint('gpt', __name__)

@gpt_routes.route('/key')
def get_key():
    print('backend gpt test')
    key = os.environ.get('GPT_SECRET_KEY')
    return {'gptAPIKey': key}
