from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models import Pagamento
import crud

router = APIRouter(prefix="/pagamentos", tags=["Pagamentos"])


@router.post("/")
def criar_pagamento(pagamento: Pagamento, session: Session = Depends(get_session)):

    session.add(pagamento)
    session.commit()
    session.refresh(pagamento)

    return {
        "id": pagamento.id,
        "pedido_id": pagamento.pedido_id,
        "valor": pagamento.valor
    }


@router.get("/")
def listar_pagamentos(session: Session = Depends(get_session)):
    return crud.listar(session, Pagamento)


@router.get("/{id}")
def buscar_pagamento(id: int, session: Session = Depends(get_session)):
    return crud.buscar(session, Pagamento, id)


@router.delete("/{id}")
def deletar_pagamento(id: int, session: Session = Depends(get_session)):
    return crud.deletar(session, Pagamento, id)