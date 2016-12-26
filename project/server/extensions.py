# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
sql = SQLAlchemy()

from flask_cache import Cache
cache = Cache()

from flask_mongoengine import MongoEngine
mongo = MongoEngine()

from flask_session import Session
session = Session()

