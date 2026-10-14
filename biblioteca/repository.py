
from biblioteca.database import carregar_livros, salvar_livros
from biblioteca.livro import Livro


class LivroRepository:
    def __init__(self, database_path=None):
        self.database_path = database_path
        self._livros = {}

        if self.database_path:
            dados = carregar_livros(self.database_path)
            for isbn, informacoes in dados.items():
                self._livros[isbn] = Livro(
                    informacoes["isbn"],
                    informacoes["titulo"],
                    informacoes["autor"],
                    informacoes["quantidade_disponivel"],
                )

    def _persistir(self):
        if self.database_path:
            salvar_livros(self.database_path, self._livros)

    def salvar(self, livro):
        if livro.isbn in self._livros:
            raise ValueError("Já existe um livro com esse ISBN.")

        self._livros[livro.isbn] = livro
        self._persistir()

    def buscar_por_isbn(self, isbn):
        livro = self._livros.get(isbn)

        if livro is None:
            raise ValueError("Livro não encontrado.")

        return livro

    def listar(self):
        return list(self._livros.values())
