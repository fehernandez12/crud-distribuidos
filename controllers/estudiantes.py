from fastapi import APIRouter, Response, status
from schemas.estudiante import Estudiante, EstudianteDto
from service.estudiante import EstudianteService

router = APIRouter()

service = EstudianteService()

@router.get("/", status_code=status.HTTP_200_OK)
async def list():
    documents = service.find_all() 
    return [doc.to_dict() for doc in documents]


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def retrieve(id: str, response: Response):
    estudiante = service.find_by_id(id)
    if estudiante.exists:
        return estudiante.to_dict()
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'El estudiante con id {id} no existe'}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(dto: EstudianteDto):
    estudiante = service.save(dto)
    return estudiante.to_dict()


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(id: str, data: EstudianteDto, response: Response):
    estudiante = service.find_by_id(id)
    if estudiante.exists:
        estudiante = service.update(id, data)
        return estudiante.to_dict()
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'El estudiante con id {id} no existe'}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id: str, response: Response):
    estudiante = service.find_by_id(id)
    if estudiante.exists:
        service.delete(id)
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'El estudiante con id {id} no existe'}
