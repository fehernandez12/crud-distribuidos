from pydantic import BaseModel, Field
import uuid

class Estudiante(BaseModel):
    id: str = Field(default=str(uuid.uuid4()), min_length=3, max_length=100)
    first_name: str = Field(..., min_length=3, max_length=100)
    last_name: str = Field(..., min_length=3, max_length=100)
    document: str = Field(..., min_length=3, max_length=100)
    phone_number: str = Field(..., min_length=3, max_length=100)

class EstudianteDto(BaseModel):
    first_name: str = Field(..., min_length=3, max_length=100)
    last_name: str = Field(..., min_length=3, max_length=100)
    document: str = Field(..., min_length=3, max_length=100)
    phone_number: str = Field(..., min_length=3, max_length=100)