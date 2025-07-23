from flask import Flask, render_template
from src.borrow.db import db
from src.borrow.borrow_controller import borrow_bp

app = Flask(__name__)
app.secret_key = 'KitHub'

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kithub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(borrow_bp)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
