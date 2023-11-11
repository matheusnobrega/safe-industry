import pika
from config import *
import pandas as pd
import ast
from classifier import knn

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

queue_name = 'class-line'
feedback_queue = 'feedback-fila'


def callback(ch, method, properties, body):
    message = body.decode('utf-8')
    print(f"Mensagem lida: {message}")
    signal = ast.literal_eval(message)

    predicted_class = knn(3, X, Y, signal)
    print(predicted_class)

    ch.basic_ack(delivery_tag=method.delivery_tag)

    if predicted_class != 0:
        # Detecção de uma condição que requer uma falha no sender1
        feedback_message = "Erro encontrado, acionar redundância"
        channel.basic_publish(
            exchange='',
            routing_key=feedback_queue,
            body=feedback_message
        )
        print(f"Forçar Falha no Sender1: {feedback_message}")
    else:
        print(f"Recebido: {message}")

channel.basic_consume(queue=queue_name, on_message_callback=callback)

print('Aguardando mensagens. Pressione CTRL+C para sair.')

channel.start_consuming()
