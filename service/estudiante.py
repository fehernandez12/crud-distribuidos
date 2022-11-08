from google.cloud.firestore_v1.query import Query
from config.database import database
from schemas.estudiante import Estudiante, EstudianteDto
from schemas.mappers import EstudianteMapper
import uuid

class EstudianteService:
    """Servicio de Estudiantes.
    
    Ejecuta todas las operaciones en base de datos."""
    def __init__(self):
        self.collection = database.collection(u'estudiantes')
        self.mapper = EstudianteMapper()

    def find_all(self):
        """Retorna todos los objetos en la colección."""
        return Query(self.collection).get()

    def find_by_id(self, id: str):
        """Retorna el objeto con el id indicado, o None
        si no existe."""
        return self.collection.document(id).get()

    def save(self, data: EstudianteDto):
        """Almacena el objeto en la base de datos."""
        object: Estudiante = self.mapper.to_entity(data)
        self.collection.document(object.id).set(object.dict())
        return self.collection.document(object.id).get()

    def update(self, id: str, data: EstudianteDto):
        """Actualiza el objeto correspondiente al id
        indicado con los datos indicados."""
        self.collection.document(id).delete()
        data_dict = data.dict()
        data_dict['id'] = id
        self.collection.document(str(id)).set(data_dict)
        return self.collection.document(id).get()

    def delete(self, id: str):
        """Elimina el objeto con el id indicado de
        la base de datos."""
        self.collection.document(id).delete()