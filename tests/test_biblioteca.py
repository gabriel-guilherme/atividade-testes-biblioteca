
from biblioteca.biblioteca import Biblioteca


def test_cadastrar_livro():
    # Arrange — preparar
    biblioteca = Biblioteca()

    # Act — executar
    livro = biblioteca.cadastrar_livro(
        "9788535902778",
        "O Senhor dos Anéis",
        "J. R. R. Tolkien",
        2,
    )

    # Assert — verificar
    assert livro.isbn == "9788535902778"
    assert livro.titulo == "O Senhor dos Anéis"
    assert livro.autor == "J. R. R. Tolkien"
    assert livro.quantidade_disponivel == 2


def test_emprestimo_reduz_quantidade():
    # Arrange
    biblioteca = Biblioteca()
    biblioteca.cadastrar_livro(
        "123",
        "Livro de Teste",
        "Autor de Teste",
        2,
    )

    # Act
    biblioteca.emprestar_livro("123")

    # Assert
    livro = biblioteca.consultar_livro("123")
    assert livro.quantidade_disponivel == 1


def test_devolucao_aumenta_quantidade():
    # Arrange
    biblioteca = Biblioteca()
    biblioteca.cadastrar_livro(
        "456",
        "Outro Livro",
        "Outro Autor",
        1,
    )
    biblioteca.emprestar_livro("456")

    # Act
    biblioteca.devolver_livro("456")

    # Assert
    livro = biblioteca.consultar_livro("456")
    assert livro.quantidade_disponivel == 1
