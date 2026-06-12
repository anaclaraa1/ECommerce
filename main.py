from fastapi import FastAPI

from database import create_db

from routers import usuarios
from routers import papeis
from routers import produtos
from routers import categorias
from routers import pedidos
from routers import pagamentos
from routers import enderecos
from routers import avaliacoes
from routers import estoque
from routers import login


app = FastAPI()

create_db()

app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(papeis.router, prefix="/papeis", tags=["Papéis"])
app.include_router(produtos.router, prefix="/produtos", tags=["Produtos"])
app.include_router(categorias.router, prefix="/categorias", tags=["Categorias"])
app.include_router(pedidos.router, prefix="/pedidos", tags=["Pedidos"])
app.include_router(pagamentos.router, prefix="/pagamentos", tags=["Pagamentos"])
app.include_router(enderecos.router, prefix="/enderecos", tags=["Endereços"])
app.include_router(avaliacoes.router, prefix="/avaliacoes", tags=["Avaliações"])
app.include_router(estoque.router, prefix="/estoque", tags=["Estoque"])
app.include_router(login.router)
