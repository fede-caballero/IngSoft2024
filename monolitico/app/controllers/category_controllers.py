from flask import jsonify, Blueprint, request
from app.services import CategoryService
from app.mapping import CategorySchema

#blueprint user
category = Blueprint('category', __name__)
category_schema = CategorySchema()

@category.route('/get-all', methods=['GET'])
def find_all():
    try:
        category_service = CategoryService()
        categories = category_service.find_all()
        serialized_categories = category_schema.dump(categories, many=True)
        return jsonify({"category": serialized_categories}), 200
    except Exception as e:
        return jsonify({"error": "Error al obtener categorias:"+str(e)}), 500

@category.route('/get/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    try:
        category_service = CategoryService()
        category = category_service.find_by_id(category_id)
        if category:
            serialized_category = category_schema.dump(category)
            return jsonify({"category": serialized_category}), 200
        else:
            return jsonify({"error": "Categoria no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": "Error al obtener categoria por ID: " + str(e)}), 500
    
@category.route('/add', methods=['POST'])
def post_category():
    category_service = CategoryService()
    category = category_schema.load(request.json)
    return {"category": category_schema.dump(category_service.create(category))}, 200

@category.route('/delete/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        cat_service = CategoryService()
        category = cat_service.find_by_id(category_id)
        if category:
            serealized_category = category_schema.dump(cat_service.delete(category_id))
            return jsonify({"category": serealized_category}, 200)
        else:
            return jsonify({"error": "Categoria no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": "Error al eliminar categoria: " + str(e)}), 500

