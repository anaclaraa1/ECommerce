from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models import Estoque
import crud

router = APIRouter(prefix="/estoque", tags=["Estoque"])


@router.post("/")
def criar_estoque(estoque: Estoque, session: Session = Depends(get_session)):

    session.add(estoque)
    session.commit()
    session.refresh(estoque)

    return {
        "id": estoque.id,
        "produto_id": estoque.produto_id,
        "quantidade": estoque.quantidade
    }


@router.get("/")
def listar_estoque(session: Session = Depends(get_session)):
    return crud.listar(session, Estoque)


@router.get("/{id}")
def buscar_estoque(id: int, session: Session = Depends(get_session)):
    return crud.buscar(session, Estoque, id)


@router.delete("/{id}")
def deletar_estoque(id: int, session: Session = Depends(get_session)):
    return crud.deletar(session, Estoque, id)