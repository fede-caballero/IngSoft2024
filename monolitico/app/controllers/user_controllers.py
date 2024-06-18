# user_controllers.py

from flask import jsonify, Blueprint, request
from app.services import UserService
from app.mapping import UserSchema

# Blueprint user
user = Blueprint('user', __name__)
user_schema = UserSchema()


def get_user_response(user, success_code=200, not_found_message="Usuario no encontrado"):
    if user:
        return jsonify({"user": user_schema.dump(user)}), success_code
    else:
        return jsonify({"error": not_found_message}), 404



def get_user_service():
    return UserService()

def handle_exception(e, message):
    return jsonify({"error": f"{message}: {str(e)}"}), 500

@user.route('/get-all', methods=['GET'])
def find_all():
    try:
        user_service = get_user_service()
        users = user_service.find_all()
        serialized_users = user_schema.dump(users, many=True)
        return jsonify({"users": serialized_users}), 200
    except Exception as e:
        return handle_exception(e, "Error al obtener usuarios")

@user.route('/get/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        user_service = get_user_service()
        user = user_service.find_by_id(user_id)
        if user:
            serialized_user = user_schema.dump(user)
            return jsonify({"user": serialized_user}), 200
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
    except Exception as e:
        return handle_exception(e, "Error al obtener usuario por ID")

@user.route('/get/<string:name>', methods=['GET'])
def find_by_name(name):
    try:
        user_service = get_user_service()
        user = user_service.find_by_name(name)
        if user:
            serialized_user = user_schema.dump(user)
            return jsonify({"user": serialized_user}), 200
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
    except Exception as e:
        return handle_exception(e, "Error al obtener usuario por nombre de usuario")

@user.route('/add', methods=['POST'])
def post_user():
    try:
        user_service = get_user_service()
        user = user_schema.load(request.json)
        return jsonify({"user": user_schema.dump(user_service.create(user))}), 200
    except Exception as e:
        return handle_exception(e, "Error al agregar usuario")

@user.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user_service = get_user_service()
        user = user_service.find_by_id(user_id)
        if user:
            serialized_user = user_schema.dump(user_service.delete(user_id))
            return jsonify({"user": serialized_user}), 200
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
    except Exception as e:
        return handle_exception(e, "Error al eliminar usuario")

@user.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user_service = get_user_service()
        user = user_service.find_by_id(user_id)
        if user:
            updated_user_data = request.json
            for key, value in updated_user_data.items():
                setattr(user, key, value)
            user_service.update(user)
            return get_user_response(user)
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
    except Exception as e:
        return handle_exception(e, "Error al actualizar usuario")