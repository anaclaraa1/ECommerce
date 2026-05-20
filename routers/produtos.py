from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models import Produto
import crud

router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.post("/")
def criar_produto(produto: Produto, session: Session = Depends(get_session)):

    session.add(produto)
    session.commit()
    session.refresh(produto)

    return {
        "id": produto.id,
        "nome": produto.nome,
        "preco": produto.preco
    }


@router.get("/")
def listar_produtos(session: Session = Depends(get_session)):
    return crud.listar(session, Produto)


@router.get("/{id}")
def buscar_produto(id: int, session: Session = Depends(get_session)):
    return crud.buscar(session, Produto, id)


@router.delete("/{id}")
def deletar_produto(id: int, session: Session = Depends(get_session)):
    return crud.deletar(session, Produto, id)