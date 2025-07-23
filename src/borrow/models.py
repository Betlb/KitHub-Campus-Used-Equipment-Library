from .db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # e.g., student, admin

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
