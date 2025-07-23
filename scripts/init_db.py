import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
from src.borrow.db import db
from src.borrow.models import User, Equipment

with app.app_context():
    db.create_all()
    print("✅ Database initialized!")

    # Seed example data
    u1 = User(name="Alice", role="student")
    e1 = Equipment(name="Camera", category="media", status="available")
    e2 = Equipment(name="Oscilloscope", category="lab", status="available")
    db.session.add_all([u1, e1, e2])
    db.session.commit()
    print("✅ Sample data added!")