# -*- coding: utf-8 -*-

from os import environ
from flask import Flask, render_template

from .extensions import sql, cache, mongo, session, api_generator

class PiCloud(Flask):

    def __init__(self, *args, **kwargs):
        super(PiCloud, self).__init__(import_name='PiCloud', *args, **kwargs)
        self.configure_app()

    def configure_app(self):
        self.configure_folders()
        self.configure_environment()
        self.configure_extensions()

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

        api_generator.init_app(self, sql)

        if self.debug:
            from flask_debugtoolbar import DebugToolbarExtension
            DebugToolbarExtension(self)

        @self.route('/')
        def welcome():
            return render_template("index.html")
