from flask import Flask
from src.borrow.borrow_controller import borrow_bp
from src.borrow.db import db

app = Flask(__name__)
app.secret_key = 'helloWorld'

# SQLite config for local
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kithub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register Blueprint
app.register_blueprint(borrow_bp)

# Home route
@app.route('/')
def home():
    return "<h1>Welcome to KitHub</h1><p><a href='/catalog'>View Equipment</a></p>"

if __name__ == '__main__':
    app.run(debug=True)
