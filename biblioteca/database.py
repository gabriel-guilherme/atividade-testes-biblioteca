import json
from pathlib import Path


def carregar_livros(caminho):
    caminho_arquivo = Path(caminho)

    if not caminho_arquivo.exists():
        return {}

    try:
        with caminho_arquivo.open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except (json.JSONDecodeError, OSError):
        return {}

    if not isinstance(dados, dict):
        return {}

    return dados


def salvar_livros(caminho, livros):
    caminho_arquivo = Path(caminho)
    caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)

    dados = {}
    for isbn, livro in livros.items():
        dados[isbn] = {
            "isbn": livro.isbn,
            "titulo": livro.titulo,
            "autor": livro.autor,
            "quantidade_disponivel": livro.quantidade_disponivel,
        }

    with caminho_arquivo.open("w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)
