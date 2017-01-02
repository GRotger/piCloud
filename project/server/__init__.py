# -*- coding: utf-8 -*-

import flask_raptor, flask_restless

from os import environ
from flask import Flask, render_template

from .models import *
from .extensions import sql, cache, mongo, session

class PiCloud(Flask):

    def __init__(self, *args, **kwargs):
        super(PiCloud, self).__init__(import_name='PiCloud', *args, **kwargs)
        self.configure_app()

    def configure_app(self):
        self.configure_folders()
        self.configure_environment()
        self.configure_extensions()
        self.configure_api()

    def configure_folders(self):
        self.template_folder = 'project/server/views'

    def configure_environment(self):
        env = environ.get('CONFIG_CLASS', 'develop')
        self.config['CONFIG_CLASS'] = env
        self.config.from_object('project.server.config.%s' % env.capitalize())

    def configure_extensions(self):
        """
        Initialize application extensions
        """
        sql.init_app(self)

        cache.init_app(self)

        mongo.init_app(self)

        session.init_app(self)

        if self.debug:
            from flask_debugtoolbar import DebugToolbarExtension
            DebugToolbarExtension(self)

    def configure_api(self):
        """
        Initialize application api
        """

        @self.route('/')
        def welcome():
            return render_template("index.html")

        self.api_manager = flask_restless.APIManager(self, flask_sqlalchemy_db=sql)
        self.api_manager.create_api(User)

        print "SUPER USEEEER %s" % self.blueprints['usersapi0'].url_prefix



