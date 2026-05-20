from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from database import get_session
from models import Papel

router = APIRouter(
    prefix="/papeis",
    tags=["Papeis"]
)


@router.post("/")
def criar_papel(
    papel: Papel,
    session: Session = Depends(get_session)
):

    session.add(papel)
    session.commit()
    session.refresh(papel)

    return {
        "id": papel.id,
        "nome": papel.nome
    }


@router.get("/")
def listar_papeis(
    session: Session = Depends(get_session)
):

    papeis = session.exec(
        select(Papel)
    ).all()

    resultado = []

    for papel in papeis:
        resultado.append({
            "id": papel.id,
            "nome": papel.nome
        })

    return resultado


@router.get("/{id}")
def buscar_papel(
    id: int,
    session: Session = Depends(get_session)
):

    papel = session.get(Papel, id)

    if not papel:
        return {"erro": "Papel não encontrado"}

    return {
        "id": papel.id,
        "nome": papel.nome
    }


@router.delete("/{id}")
def deletar_papel(
    id: int,
    session: Session = Depends(get_session)
):

    papel = session.get(Papel, id)

    if not papel:
        return {"erro": "Papel não encontrado"}

    session.delete(papel)
    session.commit()

    return {
        "mensagem": "Papel deletado"
    }