from redis_connection import r

def receber_mensagens():
    pubsub = r.pubsub()
    pubsub.subscribe('chat')

    for mensagem in pubsub.listen():
        if mensagem['type'] == 'message':
            print(mensagem['data'].decode('utf-8'))

receber_mensagens()