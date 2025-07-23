from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from ..borrow.db import db
from ..borrow.models import User
from .user_factory import UserFactory

auth_bp = Blueprint("auth", __name__, template_folder="../../templates")

# ---------- Register ----------
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name     = request.form["name"]
        role     = request.form["role"]          # radio / select
        password = request.form["password"]

        if User.query.filter_by(name=name).first():
            return render_template("register.html", error="Username already exists")

        user = UserFactory.create_user(role, name, password)
        db.session.add(user)
        db.session.commit()
        login_user(user)                         # oto‑login
        return redirect(url_for("borrow.catalog"))

    return render_template("register.html")

# ---------- Login ----------
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        user = User.query.filter_by(name=name).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("borrow.catalog"))
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

# ---------- Logout ----------
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))
