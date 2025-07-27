from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user
from src.db.db import db
from src.borrow.borrow_controller import borrow_bp
from src.auth.auth_controller import auth_bp
from src.admin.admin_controller import admin_bp
from src.db.models import User

app = Flask(__name__)
app.secret_key = 'KitHub'

# DB config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kithub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# ---- Flask‑Login ----
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(borrow_bp)
app.register_blueprint(admin_bp)

@app.route('/')
def home():
    if current_user.is_authenticated:
        if current_user.role == "admin":
            return redirect(url_for('admin.home'))
        return redirect(url_for('borrow.catalog'))
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
