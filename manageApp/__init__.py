from flask import Flask
from flask_caching import Cache
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
cache = Cache()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    global ma
    ma = Marshmallow(app)
    # 解决跨域请问题
    CORS(app, resources=r'/*')
    # 缓存
    cache.init_app(app)
    # 绑定路由
    from .routes import register
    register(app)
    return app
