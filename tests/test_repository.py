import pytest

from biblioteca import Livro, LivroRepository


@pytest.fixture
def repositorio():
    return LivroRepository()


def test_salvar_livro_no_repositorio(repositorio):
    livro = Livro("111", "Livro 1", "Autor 1", 2)

    repositorio.salvar(livro)

    assert repositorio.buscar_por_isbn("111") == livro


def test_salvar_livro_com_isbn_duplicado_levanta_erro(repositorio):
    repositorio.salvar(Livro("222", "Livro 2", "Autor 2", 1))

    with pytest.raises(ValueError, match="Já existe um livro com esse ISBN."):
        repositorio.salvar(Livro("222", "Livro 3", "Autor 3", 2))


def test_buscar_por_isbn_inexistente_levanta_erro(repositorio):
    with pytest.raises(ValueError, match="Livro não encontrado."):
        repositorio.buscar_por_isbn("999")


def test_listar_retorna_todos_os_livros(repositorio):
    livro_1 = Livro("333", "Livro A", "Autor A", 1)
    livro_2 = Livro("444", "Livro B", "Autor B", 2)

    repositorio.salvar(livro_1)
    repositorio.salvar(livro_2)

    assert repositorio.listar() == [livro_1, livro_2]
