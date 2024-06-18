from .user import User
class UserBuilder:
    def __init__(self, name, dni, email, gender, address, phone):
        self.user = User()
        self.user.name = name
        self.user.dni = dni
        self.user.email = email
        self.user.gender = gender
        self.user.address = address
        self.user.phone = phone

    def build(self):
        return self.user