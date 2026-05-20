from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models import Pedido
import crud

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.post("/")
def criar_pedido(pedido: Pedido, session: Session = Depends(get_session)):

    session.add(pedido)
    session.commit()
    session.refresh(pedido)

    return {
        "id": pedido.id,
        "usuario_id": pedido.usuario_id,
        "total": pedido.total,
        "status": pedido.status
    }


@router.get("/")
def listar_pedidos(session: Session = Depends(get_session)):
    return crud.listar(session, Pedido)


@router.get("/{id}")
def buscar_pedido(id: int, session: Session = Depends(get_session)):
    return crud.buscar(session, Pedido, id)


@router.delete("/{id}")
def deletar_pedido(id: int, session: Session = Depends(get_session)):
    return crud.deletar(session, Pedido, id)