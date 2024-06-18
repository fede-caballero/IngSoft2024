from app.models import User
from .repository_base import Read, Create, Update, Delete
from app import db


class UserRepository(Create, Read, Update, Delete):
        
        def __init__(self):
                self.__model = User

        #Read Section
        def find_all(self):
                try:
                        users = db.session.query(self.__model).all()
                        return users
                except Exception as e:
                        raise Exception("Error al obtener la lista de usuarios: " + str(e))

        
        def find_by_id(self, id):
                try:
                        entity = db.session.query(self.__model).filter(self.__model.id == id).one()
                        return entity
                except Exception as e:
                        raise Exception("Error al obtener usuario por ID: " + str(e))
        
        def find_by_name(self, name):
                try:
                        entity = db.session.query(self.__model).filter(self.__model.name == name).one()
                        return entity
                except Exception as e:
                        raise Exception("Error al obtener usuario por nombre de usuario: " + str(e))


        #Create Section
        def create(self, entity):
                db.session.add(entity)
                db.session.commit()
                return entity
         #Update Section
        def update(self, entity: User):
                db.session.merge(entity)
                db.session.commit()
                return entity

        #Delete Section
        def delete(self, id):
                entity = self.find_by_id(id)
                db.session.delete(entity)
                db.session.commit()
                return entity
        
        #Update Section
        def update(self, entity_id, updated_data):
                try:
                        user = self.find_by_id(entity_id)

                        if user:
                                for key, value in updated_data.items():
                                        setattr(user, key, value)

                                db.session.commit()
                                return user
                        else:
                                return None  # O maneja el caso donde el usuario no fue encontrado
                except Exception as e:
                        db.session.rollback()
                        raise Exception("Error al actualizar usuario: " + str(e))