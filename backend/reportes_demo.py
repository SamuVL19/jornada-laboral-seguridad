from fastapi import APIRouter
from sqlalchemy import text

router = APIRouter()

@router.get("/reportes/buscar-empleado")
def buscar_empleado_insecure(identification_code: str, db=None):
    # FALLA INTENCIONAL: SQL Injection por f-string
    query = text(f"SELECT * FROM workers WHERE identification_code = '{identification_code}'")
    return db.execute(query).fetchall()