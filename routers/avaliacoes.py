from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models import Avaliacao
import crud

router = APIRouter(prefix="/avaliacoes", tags=["Avaliacoes"])


@router.post("/")
def criar_avaliacao(avaliacao: Avaliacao, session: Session = Depends(get_session)):

    session.add(avaliacao)
    session.commit()
    session.refresh(avaliacao)

    return {
        "id": avaliacao.id,
        "nota": avaliacao.nota,
        "comentario": avaliacao.comentario
    }


@router.get("/")
def listar_avaliacoes(session: Session = Depends(get_session)):
    return crud.listar(session, Avaliacao)


@router.get("/{id}")
def buscar_avaliacao(id: int, session: Session = Depends(get_session)):
    return crud.buscar(session, Avaliacao, id)


@router.delete("/{id}")
def deletar_avaliacao(id: int, session: Session = Depends(get_session)):
    return crud.deletar(session, Avaliacao, id)