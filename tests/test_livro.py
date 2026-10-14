import pytest

from biblioteca import Livro


@pytest.mark.parametrize(
    "isbn,titulo,autor,quantidade",
    [
        ("", "Livro A", "Autor A", 1),
        ("123", "", "Autor A", 1),
        ("123", "Livro A", "", 1),
        ("123", "Livro A", "Autor A", -1),
    ],
)
def test_livro_rejeita_dados_invalidos(isbn, titulo, autor, quantidade):
    with pytest.raises(ValueError):
        Livro(isbn, titulo, autor, quantidade)


def test_livro_cria_com_dados_validos():
    livro = Livro("9788535902778", "O Senhor dos Anéis", "J. R. R. Tolkien", 2)

    assert livro.isbn == "9788535902778"
    assert livro.titulo == "O Senhor dos Anéis"
    assert livro.autor == "J. R. R. Tolkien"
    assert livro.quantidade_disponivel == 2
