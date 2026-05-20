from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models import Endereco
import crud

router = APIRouter(prefix="/enderecos", tags=["Enderecos"])


@router.post("/")
def criar_endereco(endereco: Endereco, session: Session = Depends(get_session)):

    session.add(endereco)
    session.commit()
    session.refresh(endereco)

    return {
        "id": endereco.id,
        "rua": endereco.rua,
        "cidade": endereco.cidade
    }


@router.get("/")
def listar_enderecos(session: Session = Depends(get_session)):
    return crud.listar(session, Endereco)


@router.get("/{id}")
def buscar_endereco(id: int, session: Session = Depends(get_session)):
    return crud.buscar(session, Endereco, id)


@router.delete("/{id}")
def deletar_endereco(id: int, session: Session = Depends(get_session)):
    return crud.deletar(session, Endereco, id)