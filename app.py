# app.py

# MODIFIED: Imported redirect and url_for for the homepage redirect
from flask import Flask, render_template, redirect, url_for

from src.borrow.db import db
from src.borrow.borrow_controller import borrow_bp

# MODIFIED: Imported the new admin blueprint
from src.borrow.admin_controller import admin_bp

app = Flask(__name__)
app.secret_key = 'KitHub'

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kithub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register the existing blueprint
app.register_blueprint(borrow_bp)

# MODIFIED: Register the new admin blueprint so Flask recognizes its routes
app.register_blueprint(admin_bp)


@app.route('/')
def home():
    # MODIFIED: This now redirects to the admin homepage instead of showing home.html
    return redirect(url_for('admin.home'))


if __name__ == '__main__':
    app.run(debug=True)