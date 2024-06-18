import os
from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Inicializa la extensión de SQLAlchemy
db = SQLAlchemy()

metadata = db.metadata

def create_app():
    app = Flask(__name__)
    load_dotenv()  # Carga las variables de entorno desde.env
    
    db_parameters = {
        "user": os.getenv('DB_USER'),
        "password": os.getenv('DB_PASSWORD'),
        "host": os.getenv('DB_HOST', 'localhost'),  # Se puede cambiar si es necesario
        "port": os.getenv('DB_PORT', '5432'),  # Puerto por defecto de PostgreSQL
        "dbname": os.getenv('DB_NAME')
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_parameters['user']}:{db_parameters['password']}@{db_parameters['host']}:{db_parameters['port']}/{db_parameters['dbname']}"
    
    # Inicializar la base de datos con la aplicación Flask
    db.init_app(app)

    # Inicializar Flask-Migrate
    migrate = Migrate(app)
    migrate.init_app(app, db)

    # Registrar blueprints
    from app.controllers import home, user, category, vehicle
    app.register_blueprint(home, url_prefix='')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(category, url_prefix='/category')
    app.register_blueprint(vehicle, url_prefix='/vehicle')

    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
