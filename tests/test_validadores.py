import pytest

from biblioteca.validators import validar_dados_livro


@pytest.mark.parametrize(
    "isbn,titulo,autor,quantidade",
    [
        (None, "Livro", "Autor", 1),
        ("   ", "Livro", "Autor", 1),
        ("123", None, "Autor", 1),
        ("123", "   ", "Autor", 1),
        ("123", "Livro", None, 1),
        ("123", "Livro", "   ", 1),
        ("123", "Livro", "Autor", "1"),
        ("123", "Livro", "Autor", True),
        ("123", "Livro", "Autor", -1),
    ],
)
def test_validar_dados_livro_rejeita_dados_invalidos(isbn, titulo, autor, quantidade):
    with pytest.raises(ValueError):
        validar_dados_livro(isbn, titulo, autor, quantidade)


def test_validar_dados_livro_aceita_dados_validos():
    validar_dados_livro("9781234567890", "Dom Casmurro", "Machado de Assis", 3)
