from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models import Usuario
import crud

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/")
def criar_usuario(usuario: Usuario, session: Session = Depends(get_session)):

    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    return {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email
    }


@router.get("/")
def listar_usuarios(session: Session = Depends(get_session)):
    return crud.listar(session, Usuario)


@router.get("/{id}")
def buscar_usuario(id: int, session: Session = Depends(get_session)):
    return crud.buscar(session, Usuario, id)


@router.delete("/{id}")
def deletar_usuario(id: int, session: Session = Depends(get_session)):
    return crud.deletar(session, Usuario, id)