from ..borrow.models import StudentUser, AdminUser 

class UserFactory:
    @staticmethod
    def create_user(role: str, name: str, password: str):
        role = role.lower()
        if role == "student":
            user = StudentUser(name=name, role="student")
        elif role == "admin":
            user = AdminUser(name=name, role="admin")
        else:
            raise ValueError("Unsupported role")

        user.set_password(password)
        return user
