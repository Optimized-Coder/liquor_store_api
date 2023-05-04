from ..extensions import db
from datetime import datetime
import secrets

class APIUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    api_key = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def create_api_key(self):
        self.api_key = secrets.token_urlsafe(16)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'api_key': self.api_key,
            'created_at': self.created_at
        }
