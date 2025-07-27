from ..db.models import StudentUser, AdminUser, ClubUser 

class UserFactory:
    @staticmethod
    def create_user(role: str, name: str, password: str):
        role = role.lower()
        if role == "student":
            user = StudentUser(name=name, role="student")
        elif role == "admin":
            user = AdminUser(name=name, role="admin")
        elif role == "club":
            user = ClubUser(name=name, role="club")
        else:
            raise ValueError("Unsupported role")

        user.set_password(password)
        return user
