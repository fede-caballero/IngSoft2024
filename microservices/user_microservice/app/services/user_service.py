from app.repository.user_repository import UserRepository
from app import db
from app import cache

class UserService:
    def __init__(self):
        self.__repository = UserRepository()
        
    @cache.memoize(timeout=50)
    def find_all(self):
        try:
            users = self.__repository.find_all()
            return users if users else []
        except Exception as e:
            raise Exception("An error occurred while trying to retrieve the users") from e
            
    def find_by_id(self, entity_id):
        try:
            user = cache.get(f"user_{entity_id}")
            if user is None:
                user = self.__repository.find_by_id(entity_id)
            if user:
                cache.set(f"user_{entity_id}", user, timeout=50)
                return user
        except Exception as e:
            raise Exception("An error occurred while trying to retrieve the user") from e
            
    def find_by_name(self, name):
        try:
            user = cache.get(f"user_{name}")
            if user is None:
                user = self.__repository.find_by_name(name)
            if user:
                cache.set(f"user_{name}", user, timeout=50)
                return user
        except Exception as e:
            raise Exception("An error occurred while trying to retrieve the user") from e

    def create(self, entity):
        try:
            user = self.__repository.create(entity)
            cache.set(f"user_{user.id}", user, timeout=50)
            return user
        except Exception as e:
            raise Exception("An error occurred while trying to create the user") from e

    def delete(self, entity_id):
        try:
            result = self.__repository.delete(entity_id)
            cache.delete(f"user_{entity_id}")
            return result
        except Exception as e:
            print("no funciona")
            raise Exception("An error occurred while trying to delete the user") from e
    
    def update(self, entity):
        try:
            user = self.__repository.find_by_id(entity.id)

            if user:
                user.name = entity.name
                user.dni = entity.dni
                user.email = entity.email
                user.gender = entity.gender
                user.address = entity.address
                user.phone = entity.phone

                db.session.commit()

                # Update the cache
                cache.set(f"user_{user.id}", user, timeout=50)

                return user
            else:
                return None
        except Exception as e:
            db.session.rollback()
            raise Exception("An error occurred while trying to update the user") from e