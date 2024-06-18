from app.repositories.user_repository import UserRepository
from app import db

class UserService:
    def __init__(self):
        self.__repo = UserRepository()

    def find_all(self):
        return self.__repo.find_all()

    def find_by_id(self, entity_id):
        return self.__repo.find_by_id(entity_id)

    def find_by_name(self, name):
        return self.__repo.find_by_name(name)

    def create(self, entity):
        return self.__repo.create(entity)

    def update(self, entity):
        try:
            user = self.__repo.find_by_id(entity.id)

            if user:
                user.name = entity.name
                user.dni = entity.dni
                user.email = entity.email
                user.gender = entity.gender
                user.address = entity.address  
                user.phone = entity.phone

                db.session.commit()

                return user
            else:
                return None # Devuelve None si el usuario no se encuentra
        except Exception as e:
            db.session.rollback()
            raise Exception("Error al actualizar usuario: " + str(e))

    def delete(self, entity_id):
        return self.__repo.delete(entity_id)
