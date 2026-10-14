
from dataclasses import dataclass

from biblioteca.validators import validar_dados_livro


@dataclass
class Livro:
    isbn: str
    titulo: str
    autor: str
    quantidade_disponivel: int

    def __post_init__(self):
        validar_dados_livro(
            self.isbn,
            self.titulo,
            self.autor,
            self.quantidade_disponivel,
        )
