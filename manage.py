# -*- coding: utf-8 -*-

from flask_script import Manager

from project.server import PiCloud

from project.server.extensions import sql

app     = PiCloud()
manager = Manager(app)

@manager.command
def create_db():
    """Creates the sql tables."""
    sql.create_all()

if __name__ == "__main__":
    manager.run()
