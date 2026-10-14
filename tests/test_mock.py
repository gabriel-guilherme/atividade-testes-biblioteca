from unittest.mock import patch

from biblioteca import Biblioteca


def test_biblioteca_pode_ter_repositorio_isolado_por_mock():
    with patch("biblioteca.biblioteca.LivroRepository") as repositorio_mock:
        biblioteca = Biblioteca()

        biblioteca.cadastrar_livro("777", "Livro com Mock", "Autor Mocado", 4)

        repositorio_mock.return_value.salvar.assert_called_once()
