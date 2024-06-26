from flask import Flask 
from flask_marshmallow import Marshmallow
from flask_restful import Api
from app.config import config
from pdchaos.middleware.contrib.flask.flask_middleware import FlaskMiddleware
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

ma = Marshmallow()
middleware = FlaskMiddleware()
db = SQLAlchemy()
metadata = db.metadata

def create_app() -> None:
    app = Flask(__name__)
    api = Api(app)
    
    # Carga las variables de entorno desde.env
    load_dotenv()

    # Acceso a las variables de entorno
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")


    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Construcción de la cadena de conexión utilizando las variables de entorno
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    
    # Inicialización de la base de datos
    db.init_app(app)    
    migrate = Migrate(app)
    migrate.init_app(app, db)
    
    f = config.factory('development')  # Asumiendo que 'development' es el contexto adecuado
    app.config.from_object(f)

    app.config['CHAOS_MIDDLEWARE_APPLICATION_NAME'] = 'vehicle_ms'
    app.config['CHAOS_MIDDLEWARE_APPLICATION_env'] = 'development'
    middleware.init_app(app)
    ma.init_app(app)
    
    from app.resources import home, GetAllVehicles, FindVehicleById, UpdateVehicle, AddVehicle, DeleteVehicle
    app.register_blueprint(home, url_prefix='/api/v1')
    api.add_resource(GetAllVehicles, '/get-all-vehicles')
    api.add_resource(AddVehicle, '/add-vehicle')
    api.add_resource(FindVehicleById, '/auto/<int:vehicle_id>')
    api.add_resource(DeleteVehicle, '/delete-vehicle/<int:vehicle_id>')
    api.add_resource(UpdateVehicle, '/update-vehicle/<int:vehicle_id>')
    
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app
