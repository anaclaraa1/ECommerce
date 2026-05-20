from sqlmodel import Session, select


def criar(session: Session, objeto):
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