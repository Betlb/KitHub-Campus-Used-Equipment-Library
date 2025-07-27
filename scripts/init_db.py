import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app                     
from src.db.db import db
from src.db.models import StudentUser, AdminUser, ClubUser, Equipment

def seed_data():
    # ---- Users ----
    admin   = AdminUser(name="root", role="admin")
    student1 = StudentUser(name="alice", role="student")
    student2 = StudentUser(name="bob", role="student")
    club1 = ClubUser(name="clubkit", role="club")
    club2 = ClubUser(name="techclub", role="club")

    for user in [admin, student1, student2, club1, club2]:
        user.set_password("pass")

    # ---- Equipment ----
    equipment_list = [
        Equipment(name="Camera",        category="media",     status="available"),
        Equipment(name="Oscilloscope",  category="lab",       status="available"),
        Equipment(name="Tripod",        category="media",     status="available"),
        Equipment(name="Microscope",    category="lab",       status="available"),
        Equipment(name="Laptop",        category="electronics", status="available"),
        Equipment(name="3D Printer",    category="fabrication", status="available"),
        Equipment(name="Microphone",    category="audio",     status="available"),
        Equipment(name="Lighting Kit",  category="media",     status="available"),
        Equipment(name="Soldering Station", category="lab",   status="available"),
        Equipment(name="Projector",     category="electronics", status="available")
    ]

    db.session.add_all([admin, student1, student2, club1, club2] + equipment_list)
    db.session.commit()
    print("Sample data added!")

with app.app_context():
    db.create_all()
    seed_data()
    print("Database (re)created!")
