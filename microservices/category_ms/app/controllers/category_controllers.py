from flask import jsonify, Blueprint, request
from app.services import category_service
from app.schemas import category_schema

# Blueprint para categorías
category = Blueprint('category', __name__)
category_schema = category_schema()

def get_category_service():
    return category_service()

def handle_exception(e, message):
    return jsonify({"error": f"{message}: {str(e)}"}), 500

def get_category_response(category, success_code=200, not_found_message="Categoría no encontrada"):
    if category:
        return jsonify({"category": category_schema.dump(category)}), success_code
    else:
        return jsonify({"error": not_found_message}), 404

@category.route('/get-all', methods=['GET'])
def find_all():
    try:
        category_service = get_category_service()
        categories = category_service.find_all()
        return jsonify({"category": category_schema.dump(categories, many=True)}), 200
    except Exception as e:
        return handle_exception(e, "Error al obtener categorías")

@category.route('/get/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    try:
        category_service = get_category_service()
        category = category_service.find_by_id(category_id)
        return get_category_response(category)
    except Exception as e:
        return handle_exception(e, "Error al obtener categoría por ID")

@category.route('/add', methods=['POST'])
def post_category():
    try:
        category_service = get_category_service()
        category_data = request.json
        category = category_schema.load(category_data)
        return get_category_response(category_service.create(category))
    except Exception as e:
        return handle_exception(e, "Error al agregar categoría")

@category.route('/delete/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        category_service = get_category_service()
        category = category_service.find_by_id(category_id)
        return get_category_response(category_service.delete(category_id))
    except Exception as e:
        return handle_exception(e, "Error al eliminar categoría")