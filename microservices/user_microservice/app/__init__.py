import os
from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

db = SQLAlchemy()
metadata = db.metadata
cache = Cache()

def create_app():

    app = Flask(__name__)
    load_dotenv()

    # Load the configuration
    db_parameters = {
        "user": os.getenv('DB_USER'),
        "password": os.getenv('DB_PASSWORD'),
        "host": os.getenv('DB_HOST'),
        "port": os.getenv('DB_PORT'),
        "database": os.getenv('DB_NAME')
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{db_parameters['user']}:{db_parameters['password']}@{db_parameters['host']}:{db_parameters['port']}/{db_parameters['database']}"

    # Initialize the database
    db.init_app(app)


    migrate = Migrate(app)
    migrate.init_app(app, db)

    print(db_parameters)
    #configuracion de redis

    cache_config = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_REDIS_HOST': os.getenv('REDIS_HOST'),
    'CACHE_REDIS_PORT': os.getenv('REDIS_PORT'),
    'CACHE_REDIS_DB': os.getenv('REDIS_DB'),
    'CACHE_REDIS_PASSWORD': os.getenv('REDIS_PASSWORD'),
    'CACHE_KEY_PREFIX':'user_'}

    app.config.from_mapping(cache_config)
    cache.init_app(app) #iniciar cache

#Registro de blueprints
    from app.controllers.user_controllers import user
    app.register_blueprint(user, url_prefix='/user')
    #app.register_blueprint(home, url_prefix='')
    #app.register_blueprint(category, url_prefix='/category')
    #app.register_blueprint(vehicle, url_prefix='/vehicle')

    @app.shell_context_processor
    def ctx():
        return {"app":app}
    
    return app