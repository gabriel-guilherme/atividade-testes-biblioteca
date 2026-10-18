# Mini Sistema de Biblioteca

Este projeto foi desenvolvido para atender a atividade avaliativa de Testes de Software I, com foco em:

- testes unitários com pytest;
- testes com unittest;
- uso de parametrização e fixtures;
- testes de integração entre componentes reais;
- validação de exceções e comportamento inválido;
- utilização de mock para isolar dependências;
- persistência simples em arquivo JSON.

## Estrutura do projeto

```text
atividade-testes-biblioteca/
├── biblioteca/
│   ├── __init__.py
│   ├── biblioteca.py
│   ├── database.py
│   ├── livro.py
│   ├── repository.py
│   └── validators.py
├── tests/
│   ├── test_biblioteca.py
│   ├── test_database.py
│   ├── test_integracao.py
│   ├── test_livro.py
│   ├── test_mock.py
│   ├── test_repository.py
│   ├── test_unittest.py
│   └── test_validadores.py
├── README.md
```

## Módulos e responsabilidades

### biblioteca/livro.py
Responsável pela entidade Livro. A classe `Livro` representa um livro da biblioteca e valida os dados de entrada no momento da criação.

### biblioteca/validators.py
Contém a função `validar_dados_livro`, responsável por garantir que:

- ISBN não esteja vazio;
- título não esteja vazio;
- autor não esteja vazio;
- quantidade disponível seja um inteiro válido e não negativo.

### biblioteca/repository.py
Implementa o `LivroRepository`, que armazena livros em memória e também pode persistir os dados em disco quando um caminho de arquivo é informado.

### biblioteca/database.py
Camada de persistência simples, usando `JSON`. Ela salva e recupera os livros em um arquivo `.json` para simular o armazenamento do sistema.

### biblioteca/biblioteca.py
Centraliza as operações do sistema de biblioteca, como:

- cadastrar livro;
- consultar livro por ISBN;
- verificar disponibilidade;
- emprestar livro;
- devolver livro.

## Regras de negócio implementadas

- não é possível cadastrar dois livros com o mesmo ISBN;
- não é possível consultar um livro inexistente;
- não é possível emprestar quando a quantidade disponível for zero;
- dados inválidos geram `ValueError`;
- devolução e empréstimo atualizam a quantidade disponível corretamente.

## Estrutura dos testes

### pytest
Os testes em pytest validam:

- criação do livro;
- regras de validação;
- cadastro e consulta;
- empréstimo e devolução;
- repositório;
- integração entre componentes;
- persistência em arquivo;
- uso de mock para isolar dependências.

### unittest
Existe uma classe `TestBibliotecaComUnittest` para demonstrar a mesma lógica usando a biblioteca padrão do Python.

## Como preparar o ambiente e executar

Na pasta do projeto, crie e ative um ambiente virtual:

Linux/macOS:


```bash
python -m venv .venv
source .venv/bin/activate
pip install pytest pytest-cov
```

```bash
python -m pytest -q
python -m pytest -v
python -m pytest --cov=biblioteca --cov-report=term-missing
```


```bash
python -m pytest tests/test_biblioteca.py -q
python -m pytest -k emprestimo -q
```

## Resultado verificado

A suíte foi executada com sucesso e todos os testes passaram:

```text
30 passed
```

## Interpretação do resultado

Após implementar os testes na prática neste projeto (que, apesar de pequeno, cumpre perfeitamente o seu propósito), notei os diferentes casos de uso dos testes para melhorar a robustez do software. Não apenas para evitar retrabalho, mas também para facilitar novas implementações e acelerar a descoberta de falhas, tanto no código existente quanto no que está por vir. Destaque para os diferentes casos de uso pois eu até tinha um certo conhecimento mas a matéria me mostrou diversas maneiras de abordar problemas nesse contexto.

## Teste unitário versus teste de integração (Questão final de síntese)

A diferença entre um teste unitário e um teste de integração está no nível de isolamento e no conjunto de componentes.

### Teste unitário
Um teste unitário foca em uma unidade isolada, com o objetivo de verificar o comportamento de uma função ou classe sem depender de outros módulos do sistema. No projeto, um bom exemplo é o teste da classe `Livro` em [tests/test_livro.py](tests/test_livro.py):

```python
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
```

Nesse caso, o componente testado isoladamente foi a entidade `Livro`, e a regra de validação foi verificada diretamente. A dependência relevante era a validação de dados, que foi controlada pela própria criação do objeto. O objetivo principal era descobrir defeitos como:

- ISBN vazio;
- título vazio;
- autor vazio;
- quantidade negativa;
- falha em validar entradas inválidas.

### Teste de integração
Um teste de integração verifica a interação real entre componentes do sistema, ou seja, como diferentes partes funcionam em conjunto. O melhor exemplo do projeto está em [tests/test_integracao.py](tests/test_integracao.py):

```python
def test_integracao_emprestimo_e_devolucao(biblioteca):
    biblioteca.cadastrar_livro("654", "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1)

    livro_emprestado = biblioteca.emprestar_livro("654")
    assert livro_emprestado.quantidade_disponivel == 0
    assert biblioteca.verificar_disponibilidade("654") is False

    livro_devolvido = biblioteca.devolver_livro("654")
    assert livro_devolvido.quantidade_disponivel == 1
    assert biblioteca.verificar_disponibilidade("654") is True
```

Nesse caso, os componentes utilizados de forma real foram:

- `Biblioteca`;
- `LivroRepository` em memória;
- a entidade `Livro`;
- as regras de negócio implementadas em `biblioteca.py`.

Não houve substituição de dependência: o teste usou a integração real entre os módulos para verificar se o comportamento do sistema como um todo estava correto.

### Comparação direta

Em resumo, um teste unitário responde à pergunta: “essa unidade funciona isoladamente?”, enquanto um teste de integração responde: “esses componentes funcionam corretamente juntos?”.

## Cobertura

Comando:

```bash
.venv/bin/python -m pytest --cov=biblioteca --cov-report=term-missing -q
```

Resultado verificado:

```text
..............................                                           [100%]
================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.3-final-0 ________________

Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
biblioteca/__init__.py         4      0   100%
biblioteca/biblioteca.py      26      1    96%   9
biblioteca/database.py        22      3    86%   14-15, 18
biblioteca/livro.py           10      0   100%
biblioteca/repository.py      25      0   100%
biblioteca/validators.py       9      0   100%
--------------------------------------------------------
TOTAL                         96      4    96%
30 passed in 0.18s
```


### Apresentação
https://youtu.be/1Llk8nG_N2M
