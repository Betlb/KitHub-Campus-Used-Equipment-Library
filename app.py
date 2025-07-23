from flask import Flask
from src.borrow.borrow_controller import borrow_bp

app = Flask(__name__)
app.secret_key = 'helloWorld'

# Register Blueprint
app.register_blueprint(borrow_bp)

# Home route
@app.route('/')
def home():
    return "<h1>Welcome to KitHub</h1><p><a href='/catalog'>View Equipment</a></p>"

if __name__ == '__main__':
    app.run(debug=True)
