# Exemplo Pub/Sub
Esse repositório contém um exemplo simples de um sistema que implementa uma arquitetura publish-subscribe. O projeto foi escrito 
em python e utiliza o cliente .

### Executando
1. Execute uma instância do redis, recomendo usar docker caso não possua o redis na sua máquina
```
docker run --name redis -d -p 6379:6379 redis
```
2. Crie um ambiente virtual
```
python -m venv venv
```
3. Ative o ambiente virtual
```
source venv/bin/activate
```
4. Instale as dependências do projeto
```
pip install -r requirements.txt
```
5. Execute o arquivo `sub.py` em um terminal
```
python sub.py
```
6. Abra outro terminal e execute o arquivo `pub.py`
```
python pub.py
```
7. Interaja com o terminal do `pub.py` e observe as saídas no terminal executando o `sub.py`