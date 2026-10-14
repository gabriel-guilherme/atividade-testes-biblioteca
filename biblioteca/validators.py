
def validar_dados_livro(isbn, titulo, autor, quantidade_disponivel):
    if not isinstance(isbn, str) or not isbn.strip():
        raise ValueError("O ISBN é obrigatório.")

    if not isinstance(titulo, str) or not titulo.strip():
        raise ValueError("O título é obrigatório.")

    if not isinstance(autor, str) or not autor.strip():
        raise ValueError("O autor é obrigatório.")

    if (
        not isinstance(quantidade_disponivel, int)
        or isinstance(quantidade_disponivel, bool)
        or quantidade_disponivel < 0
    ):
        raise ValueError(
            "A quantidade disponível deve ser um inteiro maior ou igual a zero."
        )
