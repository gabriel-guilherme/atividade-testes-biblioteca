import unittest

from biblioteca import Biblioteca


class TestBibliotecaComUnittest(unittest.TestCase):
    def test_cadastrar_livro(self):
        biblioteca = Biblioteca()

        # Arrange
        isbn = "555"
        titulo = "Livro em unittest"
        autor = "Autor unittest"
        quantidade = 2

        # Act
        livro = biblioteca.cadastrar_livro(isbn, titulo, autor, quantidade)

        # Assert
        self.assertEqual(livro.isbn, isbn)
        self.assertEqual(livro.titulo, titulo)
        self.assertEqual(livro.autor, autor)
        self.assertEqual(livro.quantidade_disponivel, quantidade)


if __name__ == "__main__":
    unittest.main()
