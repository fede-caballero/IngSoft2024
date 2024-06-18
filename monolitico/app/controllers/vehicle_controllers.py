from flask import jsonify, Blueprint, request
from app.services import VehicleService
from app.mapping import VehicleSchema

#blueprint vehicle
vehicle = Blueprint('vehicle', __name__)
vehicle_schema = VehicleSchema()
vehicle_service = VehicleService()

def handle_exception(e, message):
    return jsonify({"error": f"{message}: {str(e)}"}), 500

@vehicle.route('/get-all', methods=['GET'])
def find_all():
    try:
        vehicles = vehicle_service.find_all()
        serialized_users = vehicle_schema.dump(vehicles, many=True)
        return jsonify({"user": serialized_users}), 200
    except Exception as e:
        return handle_exception(e, "Error al Obtener Vehiculos")
@vehicle.route('/add', methods=['POST'])
def post_vehicle():
    try:
        vehicle = vehicle_schema.load(request.json)
        return {"vehicle": vehicle_schema.dump(vehicle_service.create(vehicle))}, 200
    except Exception as e:
        return handle_exception(e, "Error al agregar Vehiculo")

@vehicle.route('/delete/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    try:
        vehicle = vehicle_service.find_by_id(vehicle_id)
        if vehicle:
            serialized_vehicle = vehicle_schema.dump(vehicle_service.delete(vehicle_id))
            return jsonify({"vehicle": serialized_vehicle}, 200)
        else:
            return jsonify({"error": "Vehiculo no encontrado"}), 404
    except Exception as e:
        return handle_exception(e, "Error al obtener el vehiculo")
@vehicle.route('/update/<int:vehicle_id>', methods=['PUT'])
def update_vehicle(vehicle_id):
    try:
        vehicle = vehicle_service.find_by_id(vehicle_id)
        if vehicle:
            updated_vehicle_data = request.json
            for key, value in updated_vehicle_data.items():
                setattr(vehicle, key, value)
            vehicle_service.update(vehicle)
            serialized_vehicle = vehicle_schema.dump(vehicle)
            return jsonify({"vehicle": serialized_vehicle}), 200
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
    except Exception as e:
        return handle_exception(e, "Error al actualizar Vehiculo")