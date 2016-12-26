

import flask_raptor

from os import environ
from flask import Flask

from .extensions import sql, cache, mongo, session

class PiCloud(Flask):

    def __init__(self, *args, **kwargs):
        super(PiCloud, self).__init__(import_name='PiCloud', *args, **kwargs)
        self.configure_app()

    def configure_app(self):
        self.configure_environment()
        self.configure_extensions()
        self.configure_rest()

    def configure_environment(self):
        env = environ.get('CONFIG_CLASS', 'develop')
        self.config['CONFIG_CLASS'] = env
        self.config.from_object('project.server.config.%s' % env)

    def configure_extensions(self):
        """
        Initialize application extensions
        """
        sql.init_app(self)

        cache.init_app(self)

        mongo.init_app(self)

        session.init_app(self)

        flask_raptor.init_app(self)


    def configure_rest(self):
        pass
