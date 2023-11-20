from dependencies import db
from modules.common.models import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.name