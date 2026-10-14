
from biblioteca.livro import Livro
from biblioteca.repository import LivroRepository


class Biblioteca:
    def __init__(self, repositorio=None, database_path=None):
        if repositorio is not None:
            self.repositorio = repositorio
        else:
            self.repositorio = LivroRepository(database_path=database_path)

    def cadastrar_livro(self, isbn, titulo, autor, quantidade_disponivel):
        livro = Livro(isbn, titulo, autor, quantidade_disponivel)
        self.repositorio.salvar(livro)
        return livro

    def consultar_livro(self, isbn):
        return self.repositorio.buscar_por_isbn(isbn)

    def verificar_disponibilidade(self, isbn):
        livro = self.consultar_livro(isbn)
        return livro.quantidade_disponivel > 0

    def emprestar_livro(self, isbn):
        livro = self.consultar_livro(isbn)

        if livro.quantidade_disponivel == 0:
            raise ValueError("Não há exemplares disponíveis para empréstimo.")

        livro.quantidade_disponivel -= 1
        return livro

    def devolver_livro(self, isbn):
        livro = self.consultar_livro(isbn)
        livro.quantidade_disponivel += 1
        return livro
