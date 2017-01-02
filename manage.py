# -*- coding: utf-8 -*-

from flask_script import Manager

from project.server import PiCloud

app     = PiCloud()
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
