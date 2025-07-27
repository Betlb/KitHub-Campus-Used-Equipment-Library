import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app                     
from src.db.db import db
from src.db.models import StudentUser, AdminUser, ClubUser, Equipment

def seed_data():
    admin   = AdminUser(name="root",   role="admin")
    student = StudentUser(name="alice", role="student")
    club = ClubUser(name="clubkit", role="club")
    admin.set_password("pass")          
    student.set_password("pass")
    club.set_password("pass")

    cam  = Equipment(name="Camera",        category="media", status="available")
    osc  = Equipment(name="Oscilloscope",  category="lab",   status="available")

    db.session.add_all([admin, student, cam, osc])
    db.session.commit()
    print("Sample data added!")

with app.app_context():
    db.create_all()
    seed_data()
    print("Database (re)created!")
