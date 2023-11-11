from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import time
import pika
from config import *
import random
import time
import os

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def make_connection():
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    return channel


def display_message(message):
    socketio.emit('update_message', {'message': message})


def generate_random_message():
    channel = make_connection()

    queue_name = 'class-line'
    feedback_queue = 'feedback-fila'
    channel.queue_declare(queue=feedback_queue)

    while True:

        message = str(X[random.randint(0, len(X) - 1)])
        channel.queue_declare(queue=queue_name)
        channel.basic_publish(exchange='', routing_key=queue_name, body=message)

        display_message(f'Sinais gerados: {message}')
        time.sleep(5)

        method_frame, header_frame, body = channel.basic_get(queue=feedback_queue, auto_ack=True)
        if method_frame:
            feedback_message = body.decode('utf-8')
            if "Erro" in feedback_message:
                print("Feedback de falha recebido. Simulando uma falha.")
                display_message(f'Falha detectada!')
                
                time.sleep(5)
                os._exit(0)

if __name__ == '__main__':
    # Inicie a função de geração em uma thread separada
    from threading import Thread
    generator_thread = Thread(target=generate_random_message)
    generator_thread.start()

    # Inicie o servidor Flask-SocketIO
    socketio.run(app, debug=True)
