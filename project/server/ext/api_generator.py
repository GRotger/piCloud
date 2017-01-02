# -*- coding: utf-8 -*-

import flask_restless

from ..models import User

class ApiGenerator(object):
    """
    Application Api Generator
    """

    def __init__(self, app = None):
        if app:
            self.init_app(app)

    def init_app(self, app, sql):
        self.api_manager = flask_restless.APIManager(app, flask_sqlalchemy_db=sql)

        api_configs = [
            {
                'model': User,
                'url_prefix': '/api/v2',
                'methods': ['GET', 'POST']
            }
        ]
        #
        # for config in api_configs:
        #     self.api_manager.create_api(config.get('model'), **config)
