from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models import Categoria
import crud

router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.post("/")
def criar_categoria(categoria: Categoria, session: Session = Depends(get_session)):

    session.add(categoria)
    session.commit()
    session.refresh(categoria)

    return {
        "id": categoria.id,
        "nome": categoria.nome
    }


@router.get("/")
def listar_categorias(session: Session = Depends(get_session)):
    return crud.listar(session, Categoria)


@router.get("/{id}")
def buscar_categoria(id: int, session: Session = Depends(get_session)):
    return crud.buscar(session, Categoria, id)


@router.delete("/{id}")
def deletar_categoria(id: int, session: Session = Depends(get_session)):
    return crud.deletar(session, Categoria, id)