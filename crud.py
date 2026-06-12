from sqlmodel import Session, select
from routers.auth import password_hash
from models import Usuario


def criar(session: Session, objeto):

    if isinstance(objeto, Usuario):
        objeto.senha_hash = password_hash.hash(
            objeto.senha_hash
        )

    session.add(objeto)
    session.commit()
    session.refresh(objeto)

    return objeto


def listar(session: Session, model):
    return session.exec(select(model)).all()


def buscar(session: Session, model, id):
    return session.get(model, id)


def deletar(session: Session, model, id):
    obj = session.get(model, id)

    if obj:
        session.delete(obj)
        session.commit()

    return {"mensagem": "Deletado com sucesso"}