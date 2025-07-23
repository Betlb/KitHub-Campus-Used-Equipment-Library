from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .db import db

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    role = db.Column(db.String(20))         # student / admin
    password_hash = db.Column(db.String(128))
    type = db.Column(db.String(20))         # STI ayırıcısı
    __mapper_args__ = {"polymorphic_on": type, "polymorphic_identity": "user"}

    # ➜ parola yardımcıları
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class StudentUser(User):
    __mapper_args__ = {"polymorphic_identity": "student"}

class AdminUser(User):
    __mapper_args__ = {"polymorphic_identity": "admin"}

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    category = db.Column(db.String(32), nullable=False)
    status = db.Column(db.String(16), default="available")  # available / borrowed

class BorrowRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
    start_date = db.Column(db.String(32))
    end_date = db.Column(db.String(32))
    status = db.Column(db.String(16), default="pending")  # pending / approved / rejected
    notes = db.Column(db.Text)

    user = db.relationship('User')
    equipment = db.relationship('Equipment')
