# Introdução
Repositório padrão de projetos utilizando a ferramenta Poetry como gerenciador de dependências.

Os arquivos .yaml são configurações das dependências padrões, assim como .toml e .lock são configurações do Poetry.


# Primeiros passos
1.	Instalação

    - Clone o repositório em uma pasta local

        `git clone <repo_url>`

    - Execute o poetry para criar o ambiente virtual com as dependências do projeto

        `poetry install`

    - Executar a instalação do pre-commit

        `poetry run pre-commit install --hook-type pre-commit --hook-type commit-msg --hook-type pre-push`

2.	Dependências de software
    - Python v. 3.10+ instalado
    - Poetry 1.1+ instalado

# Testes
Os gatilhos de execução padrão das formatações serão o git commit e git push.


# TODO
Implementar mais configurações de acordo com a demanda dos projetos.

- [Extra flake8 extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions)
- [Useful poetry commands](https://pythonbiellagroup.it/en/gestire-dipendenze/poetry-advance/)
- [Poetry Documentation](https://python-poetry.org/docs/)
