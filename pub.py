from redis_connection import r
from datetime import datetime


def enviar_mensagem(usuario, mensagem):
    tempo_atual = datetime.now().strftime("%H:%M:%S")
    mensagem_formatada = f"[{tempo_atual}] [{usuario}]: {mensagem}"
    r.publish('chat', mensagem_formatada)


nome_usuario = input("Digite seu nome de usuário: ")

enviar_mensagem(nome_usuario, "entrou no chat!")

try:
    while True:
        mensagem = input()
        enviar_mensagem(nome_usuario, mensagem)
except KeyboardInterrupt:
    enviar_mensagem(nome_usuario, "saiu do chat!")
