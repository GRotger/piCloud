# -*- coding: utf-8 -*-

class Config(object):
    DEBUG   = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class Production(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class Develop(Config):
    DEBUG = True

