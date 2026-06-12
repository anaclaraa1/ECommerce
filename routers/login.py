from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select

from database import get_session
from models import Usuario
from routers.auth import (
    create_access_token,
    password_hash
)

router = APIRouter(
    prefix="/login",
    tags=["Login"]
)

@router.post("/")
def login(
    form: OAuth2PasswordRequestForm = Depends(),
    session=Depends(get_session)
):

    usuario = session.exec(
        select(Usuario).where(
            Usuario.email == form.username
        )
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=400,
            detail="Usuário ou senha inválidos"
        )

    if not password_hash.verify(
        form.password,
        usuario.senha_hash
    ):
        raise HTTPException(
            status_code=400,
            detail="Usuário ou senha inválidos"
        )

    access_token = create_access_token(
        {"sub": usuario.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }