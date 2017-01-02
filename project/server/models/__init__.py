
from ..extensions import sql

class User(sql.Model):
    __tablename__ = "users"

    id            = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    email         = sql.Column(sql.String(255), unique=True, nullable=False)
    password      = sql.Column(sql.String(255), nullable=False)
    registered_on = sql.Column(sql.DateTime, nullable=False)
    admin          = sql.Column(sql.Boolean, nullable=False, default=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {0}>'.format(self.email)
