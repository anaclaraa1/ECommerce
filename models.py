from sqlmodel import SQLModel, Field, Relationship
from decimal import Decimal
from typing import Optional
from datetime import datetime


class UsuarioPapel(SQLModel, table=True):
    __tablename__ = "usuario_papeis"

    usuario_id: int = Field(
        foreign_key="usuarios.id",
        primary_key=True
    )

    papel_id: int = Field(
        foreign_key="papeis.id",
        primary_key=True
    )


class ProdutoCategoria(SQLModel, table=True):
    __tablename__ = "produto_categorias"

    produto_id: int = Field(
        foreign_key="produtos.id",
        primary_key=True
    )

    categoria_id: int = Field(
        foreign_key="categorias.id",
        primary_key=True
    )


class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"

    id: Optional[int] = Field(default=None, primary_key=True)

    nome: str = Field(max_length=100)

    email: str = Field(
        max_length=150,
        unique=True
    )

    senha_hash: str = Field(max_length=255)

    criado_em: datetime = Field(
        default_factory=datetime.now
    )

    pedidos: list["Pedido"] = Relationship(
        back_populates="usuario"
    )

    enderecos: list["Endereco"] = Relationship(
        back_populates="usuario"
    )

    avaliacoes: list["Avaliacao"] = Relationship(
        back_populates="usuario"
    )

    papeis: list["Papel"] = Relationship(
        back_populates="usuarios",
        link_model=UsuarioPapel
    )


class Papel(SQLModel, table=True):
    __tablename__ = "papeis"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    nome: str = Field(
        max_length=50,
        unique=True
    )

    usuarios: list["Usuario"] = Relationship(
        back_populates="papeis",
        link_model=UsuarioPapel
    )


class Produto(SQLModel, table=True):
    __tablename__ = "produtos"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    nome: str = Field(max_length=150)

    descricao: str

    preco: Decimal = Field(
        max_digits=10,
        decimal_places=2
    )

    criado_em: datetime = Field(
        default_factory=datetime.now
    )

    avaliacoes: list["Avaliacao"] = Relationship(
        back_populates="produto"
    )

    estoque: Optional["Estoque"] = Relationship(
        back_populates="produto"
    )

    categorias: list["Categoria"] = Relationship(
        back_populates="produtos",
        link_model=ProdutoCategoria
    )

    itens_pedido: list["ItemPedido"] = Relationship(
        back_populates="produto"
    )


class Categoria(SQLModel, table=True):
    __tablename__ = "categorias"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    nome: str = Field(max_length=100)

    produtos: list["Produto"] = Relationship(
        back_populates="categorias",
        link_model=ProdutoCategoria
    )


class Pedido(SQLModel, table=True):
    __tablename__ = "pedidos"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    usuario_id: int = Field(
        foreign_key="usuarios.id"
    )

    total: Decimal = Field(
        max_digits=10,
        decimal_places=2
    )

    status: str = Field(max_length=50)

    criado_em: datetime = Field(
        default_factory=datetime.now
    )

    usuario: "Usuario" = Relationship(
        back_populates="pedidos"
    )

    pagamentos: list["Pagamento"] = Relationship(
        back_populates="pedido"
    )

    itens: list["ItemPedido"] = Relationship(
        back_populates="pedido"
    )


class ItemPedido(SQLModel, table=True):
    __tablename__ = "itens_pedido"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    pedido_id: int = Field(
        foreign_key="pedidos.id"
    )

    produto_id: int = Field(
        foreign_key="produtos.id"
    )

    quantidade: int

    preco: Decimal = Field(
        max_digits=10,
        decimal_places=2
    )

    pedido: "Pedido" = Relationship(
        back_populates="itens"
    )

    produto: "Produto" = Relationship(
        back_populates="itens_pedido"
    )


class Pagamento(SQLModel, table=True):
    __tablename__ = "pagamentos"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    pedido_id: int = Field(
        foreign_key="pedidos.id"
    )

    valor: Decimal = Field(
        max_digits=10,
        decimal_places=2
    )

    metodo: str = Field(max_length=50)

    status: str = Field(max_length=50)

    pago_em: Optional[datetime] = None

    pedido: "Pedido" = Relationship(
        back_populates="pagamentos"
    )


class Endereco(SQLModel, table=True):
    __tablename__ = "enderecos"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    usuario_id: int = Field(
        foreign_key="usuarios.id"
    )

    rua: str = Field(max_length=150)

    cidade: str = Field(max_length=100)

    estado: str = Field(max_length=100)

    cep: str = Field(max_length=20)

    usuario: "Usuario" = Relationship(
        back_populates="enderecos"
    )


class Avaliacao(SQLModel, table=True):
    __tablename__ = "avaliacoes"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    usuario_id: int = Field(
        foreign_key="usuarios.id"
    )

    produto_id: int = Field(
        foreign_key="produtos.id"
    )

    nota: int

    comentario: str

    criado_em: datetime = Field(
        default_factory=datetime.now
    )

    usuario: "Usuario" = Relationship(
        back_populates="avaliacoes"
    )

    produto: "Produto" = Relationship(
        back_populates="avaliacoes"
    )


class Estoque(SQLModel, table=True):
    __tablename__ = "estoque"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    produto_id: int = Field(
        foreign_key="produtos.id",
        unique=True
    )

    quantidade: int

    atualizado_em: datetime = Field(
        default_factory=datetime.now
    )

    produto: "Produto" = Relationship(
        back_populates="estoque"
    )
