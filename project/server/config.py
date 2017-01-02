# -*- coding: utf-8 -*-

from os import getenv

class Config(object):
    SECRET_KEY = "@%i!s)z)xufz&995i+)bu19mr)7e6)hfhb_#^7b*)mwi&7@qf"

    DEBUG   = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

    MONGODB_HOST = 'mongo'

    DEBUG_TB_PANELS = [
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',

        # Add the MongoDB panel
        # 'flask_debugtoolbar_mongo.panel.MongoDebugPanel'
    ]

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:'+ getenv('MYSQL_ROOT_PASSWORD', 'password') +'@'+ getenv('MYSQL_PORT_3306_TCP_ADDR', '127.0.0.1') + '/picloud'
    SQLALCHEMY_ECHO = False

class Production(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class Develop(Config):
    DEBUG = True




