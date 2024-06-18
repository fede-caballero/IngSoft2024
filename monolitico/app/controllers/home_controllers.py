from flask import jsonify, Blueprint

#definimos el home

#blueprint home
home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to the API REST'}, 200)