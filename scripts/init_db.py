import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app                     
from src.db.db import db
from src.db.models import StudentUser, AdminUser, Equipment

def seed_data():
    # ---- Users ----
    admin   = AdminUser(name="root",   role="admin")
    student = StudentUser(name="alice", role="student")
    admin.set_password("pass")          
    student.set_password("pass")

    # ---- Equipment ----
    cam  = Equipment(name="Camera",        category="media", status="available")
    osc  = Equipment(name="Oscilloscope",  category="lab",   status="available")

    db.session.add_all([admin, student, cam, osc])
    db.session.commit()
    print("Sample data added!")

with app.app_context():
    db.create_all()
    seed_data()
    print("Database (re)created!")
