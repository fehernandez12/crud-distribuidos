from .estudiante import Estudiante, EstudianteDto

class EstudianteMapper:
    def to_dto(self, entity: Estudiante):
        return EstudianteDto(
            first_name=entity.first_name,
            last_name=entity.last_name,
            document=entity.document,
            phone_number=entity.phone_number,
        )

    def to_entity(self, dto: EstudianteDto):
        return Estudiante(
            first_name=dto.first_name,
            last_name=dto.last_name,
            document=dto.document,
            phone_number=dto.phone_number,
        )