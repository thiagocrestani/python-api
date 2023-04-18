# Python API

## Descrição
Este é um web service RESTful que permite a leitura da lista de indicados e vencedores
da categoria Pior Filme do Golden Raspberry Awards.

## Requisitos
- Python 3.8 ou superior (https://realpython.com/installing-python/)
- pip e virtualenv (https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- Git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/)

## Instalação
1. Clone o repositório em sua máquina local:
```bash
git clone https://github.com/thiagocrestani/python-api.git
```
2. Entre na pasta do projeto:
```bash
cd python-api
```
3. Crie um ambiente virtual e ative-o:
```bash
python3 -m venv venv
source venv/bin/activate (no Windows: venv\Scripts\activate)
```
4. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```


## Executando o projeto
Para executar o projeto, basta rodar o seguinte comando na raiz do projeto:
```bash
uvicorn api.app:app --reload
```
Com o servidor rodando, você pode acessar o endpoint do web service através do endereço: `http://localhost:8000/producers_max_min_interval.


## Endpoints
Os endpoints foram implementados seguindo a seguinte estrutura:

| Metodo HTTP| Recurso                                     | Descrição                              |
| -------- | ---------------------------------------- | ---------------------------------------- |
| `GET`    | `/producers_max_min_interval`            | Retorna os produtores com o maior e o menor intervalo entre prêmios|


## Testes de integração
Os testes de integração foram implementados com o Pytest. Para executar os testes, basta rodar o seguinte comando na raiz do projeto:
```bash
pytest
```

Lembre-se que o projeto deve estar rodando e o ambiente virtual criado deve estar ativo (`source venv/bin/activate`)

Os testes garantem que os dados obtidos estão de acordo com os dados fornecidos na proposta.




