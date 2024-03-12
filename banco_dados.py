from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from enum import Enum


class tipo_acesso(Enum):
    Admin = 1
    User = 2
    


@dataclass
class Usuario:
    login: str
    senha: str
    nome: str
    tipo_acesso : tipo_acesso = tipo_acesso.User

@dataclass
class Produto:
        cod_barras: str
        nome: str
        descricao: str
        quantidade: int
        valor_compra: float
        valor_venda: float
        fornecedor: Optional['Fornecedor'] = None
        categoria: Optional['Categoria'] = None

@dataclass
class MovimentacaoEstoque:
        id_movimentacao: int
        cod_barras: str
        data: datetime
        quantidade: int
        tipo_movimentacao: str

@dataclass
class Valor:
        valor_compra: float
        valor_venda: float

@dataclass
class Fornecedor:
        nome: str
        endereco: str
        telefone: str
        email: str

@dataclass
class Categoria:
        nome: str
        subcategoria: Optional['Subcategoria'] = None

@dataclass
class Subcategoria:
        nome: str


class RepositorioAbstrato(ABC):
    
    @abstractmethod 
    def salvar_usuario(self, usuario: Usuario) -> None: pass


    @abstractmethod 
    def buscar_usuario_por_login(self, login: str) -> Optional[Usuario]: pass

    @abstractmethod 
    def salvar_produto(self, produto: Produto) -> None: pass

    @abstractmethod 
    def buscar_produto_por_cod_barras(self, cod_barras: str) -> Optional[Produto]: pass

    @abstractmethod 
    def salvar_movimentacao_estoque(self, movimentacao: MovimentacaoEstoque) -> None: pass

    @abstractmethod 
    def buscar_movimentacoes_estoque_por_cod_barras(self, cod_barras: str) -> List[MovimentacaoEstoque]: pass

    @abstractmethod 
    def salvar_valor(self, valor: Valor) -> None: pass

    @abstractmethod 
    def buscar_valor_por_cod_barras(self, cod_barras: str) -> Optional[Valor]: pass

    @abstractmethod 
    def salvar_fornecedor(self, fornecedor: Fornecedor) -> None: pass

    @abstractmethod 
    def buscar_fornecedor_por_nome(self, nome: str) -> Optional[Fornecedor]: pass

    @abstractmethod 
    def salvar_categoria(self, categoria: Categoria) -> None: pass

    @abstractmethod 
    def buscar_categoria_por_nome(self, nome: str) -> Optional[Categoria]: pass

    @abstractmethod 
    def salvar_subcategoria(self, subcategoria: Subcategoria) -> None: pass

                        
"""class RepositorioConcreto(RepositorioAbstrato):
    def __init__(self):
        self.usuarios = []
        self.produtos = []
        self.movimentacoes_estoque = []
        self.valores = []
        self.fornecedores = []
        self.categorias = []
        self.subcategorias = []

    def salvar_usuario(self, usuario: Usuario) -> None:
        self.usuarios.append(usuario)"""
        
class RepositorioConcreto(RepositorioAbstrato):
    def __init__(self):
        self.usuarios = []
        self.produtos = []
        self.movimentacoes_estoque = []
        self.valores = []
        self.fornecedores = []
        self.categorias = []
        self.subcategorias = []

    def salvar_usuario(self, usuario: Usuario) -> None:
        if not self.buscar_usuario_por_login(usuario.login):
            self.usuarios.append(usuario)
        else:
            print(f"Usuário com login '{usuario.login}' já existe. Usuário não foi salvo.")

    """def buscar_usuario_por_login(self, login: str) -> Optional[Usuario]:
        return next"""

    def buscar_usuario_por_login(self, login: str) -> Optional[Usuario]:
        return next((u for u in self.usuarios if u.login == login), None)

    def salvar_produto(self, produto: Produto) -> None:
        if not self.buscar_produto_por_cod_barras(produto.cod_barras):
            self.produtos.append(produto)
        else:
            print(f"Produto com código de barras '{produto.cod_barras}' já existe. Produto não foi salvo.")
    
    """def salvar_produto(self, produto: Produto) -> None:
        self.produtos.append(produto)"""

    def buscar_produto_por_cod_barras(self, cod_barras: str) -> Optional[Produto]:
        return next((p for p in self.produtos if p.cod_barras == cod_barras), None)

    def salvar_movimentacao_estoque(self, movimentacao: MovimentacaoEstoque) -> None:
        self.movimentacoes_estoque.append(movimentacao)

    def buscar_movimentacoes_estoque_por_cod_barras(self, cod_barras: str) -> List[MovimentacaoEstoque]:
        return [m for m in self.movimentacoes_estoque if m.cod_barras == cod_barras]

    def salvar_valor(self, valor: Valor) -> None:
        self.valores.append(valor)
    
    def buscar_valor_por_cod_barras(self, cod_barras: str) -> Optional[Valor]:
        return next((v for v in self.valores if v.cod_barras == cod_barras), None)

    def salvar_fornecedor(self, fornecedor: Fornecedor) -> None:
        self.fornecedores.append(fornecedor)

    def buscar_fornecedor_por_nome(self, nome: str) -> Optional[Fornecedor]:
        return next((f for f in self.fornecedores if f.nome == nome), None)

    def salvar_categoria(self, categoria: Categoria) -> None:
        self.categorias.append(categoria)

    def buscar_categoria_por_nome(self, nome: str) -> Optional[Categoria]:
        return next((c for c in self.categorias if c.nome == nome), None)

    def salvar_subcategoria(self, subcategoria: Subcategoria) -> None:
        self.subcategorias.append(subcategoria)
        
        
    def adicionar_produto(repositorio):
        
        cod_barras = input("Digite o código de barras: ")

        # Check o produto para ver se o cod_barras existe
        produto_existe = repositorio.buscar_produto_por_cod_barras(cod_barras)

        if produto_existe:
            print(f"Produto com código de barras '{cod_barras}' já existe. Não foi possível adicionar o produto.")
            return

        # Se nao existir, continua o restante da funcao
        nome = input("Digite o nome do produto: ")
        descricao = input("Digite a descrição: ")
        quantidade = int(input("Digite a quantidade: "))
        valor_compra = float(input("Digite o valor de compra: "))
        valor_venda = float(input("Digite o valor de venda: "))
        fornecedor_nome = input("Digite o nome do fornecedor: ")
        fornecedor = Fornecedor(nome=fornecedor_nome, endereco='Fornecedor Endereço', telefone='123456789', email='fornecedor@exemplo.com')
        categoria_nome = input("Digite o nome da categoria: ")
        categoria = Categoria(nome=categoria_nome)

        repositorio.salvar_fornecedor(fornecedor)
        repositorio.salvar_categoria(categoria)

        produto = Produto(
            cod_barras=cod_barras,
            nome=nome,
            descricao=descricao,
            quantidade=quantidade,
            valor_compra=valor_compra,
            valor_venda=valor_venda,
            fornecedor=fornecedor,
            categoria=categoria,
        )

        repositorio.salvar_produto(produto)
        print(f"Produto '{nome}' adicionado com sucesso!")
        
# Instanciando o  RepositorioConcreto
repositorio = RepositorioConcreto()

# Adicionando produtos
repositorio.adicionar_produto()
repositorio.adicionar_produto()


