import json

from flask import Blueprint, jsonify, request, redirect , send_file

from src.app.app_bo import APP_BO
app_bo = APP_BO()

users_blueprint = Blueprint('users', __name__, url_prefix='/users/api/v1')


@users_blueprint.route('/ping')
def index():
    return jsonify({'status': 'Welcome Users!'})

@users_blueprint.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        data,html= app_bo.main(file=file)
        # print(data,html)
        return send_file(data, download_name='data.xlsx', as_attachment=True)
    except Exception as ex:
        print(ex)
        return jsonify({'status': 'Fail!'})

@users_blueprint.route('/search', methods=['POST'])
def search():
    try:
        data = json.loads(request.data)
        print(data)
        domain = str(data['input']).strip()
        response = app_bo.search(domain)
        return response
    except Exception as ex:
        print(ex)
        return jsonify({'status': 'Fail!'})