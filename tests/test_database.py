import json

import pytest

from biblioteca import Biblioteca


@pytest.fixture
def caminho_temporario(tmp_path):
    return tmp_path / "biblioteca.json"


def test_persistencia_salva_e_recupera_livros(caminho_temporario):
    biblioteca = Biblioteca(database_path=str(caminho_temporario))
    biblioteca.cadastrar_livro("111", "Livro Persistido", "Autor", 3)

    dados = json.loads(caminho_temporario.read_text(encoding="utf-8"))

    assert dados["111"]["titulo"] == "Livro Persistido"
    assert dados["111"]["quantidade_disponivel"] == 3

    outra_biblioteca = Biblioteca(database_path=str(caminho_temporario))
    livro = outra_biblioteca.consultar_livro("111")

    assert livro.titulo == "Livro Persistido"
    assert livro.quantidade_disponivel == 3
