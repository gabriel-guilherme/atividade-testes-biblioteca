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
└── Atividade_Avaliativa_Unidade_1_Testes_de_Software.docx.pdf
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

## Como executar

```bash
cd atividade-testes-biblioteca
.venv/bin/python -m pytest -q
```

## Resultado verificado

A suíte foi executada com sucesso e todos os testes passaram:

```text
27 passed in 0.05s
```

## Interpretação do resultado

Após implementar os testes na prática neste projeto (que, apesar de pequeno, cumpre perfeitamente o seu propósito), notei os diferentes casos de uso dos testes para melhorar a robustez do software. Não apenas para evitar retrabalho, mas também para facilitar novas implementações e acelerar a descoberta de falhas, tanto no código existente quanto no que está por vir. Destaque para os diferentes casos de uso pois eu até tinha um certo conhecimento mas a matéria me mostrou diversas maneiras de abordar problemas nesse contexto.