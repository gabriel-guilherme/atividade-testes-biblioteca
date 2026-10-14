import pytest

from biblioteca import Biblioteca, Livro


@pytest.fixture
def biblioteca():
    return Biblioteca()


def test_integracao_cadastro_consulta_e_disponibilidade(biblioteca):
    livro = biblioteca.cadastrar_livro("321", "Alice no País das Maravilhas", "Lewis Carroll", 1)

    assert biblioteca.consultar_livro("321") == livro
    assert biblioteca.verificar_disponibilidade("321") is True


def test_integracao_emprestimo_e_devolucao(biblioteca):
    biblioteca.cadastrar_livro("654", "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1)

    livro_emprestado = biblioteca.emprestar_livro("654")
    assert livro_emprestado.quantidade_disponivel == 0
    assert biblioteca.verificar_disponibilidade("654") is False

    livro_devolvido = biblioteca.devolver_livro("654")
    assert livro_devolvido.quantidade_disponivel == 1
    assert biblioteca.verificar_disponibilidade("654") is True


def test_integracao_emprestimo_sem_exemplar_disponivel_levanta_erro(biblioteca):
    biblioteca.cadastrar_livro("987", "Livro sem estoque", "Autor", 0)

    with pytest.raises(ValueError, match="Não há exemplares disponíveis para empréstimo."):
        biblioteca.emprestar_livro("987")


def test_integracao_consulta_livro_inexistente_levanta_erro(biblioteca):
    with pytest.raises(ValueError, match="Livro não encontrado."):
        biblioteca.consultar_livro("000")


def test_importa_classes_pelo_pacote_raiz():
    assert Biblioteca is not None
    assert Livro is not None
