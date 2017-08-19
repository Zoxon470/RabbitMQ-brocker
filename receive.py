import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='text')

def callback(ch, method, properties, body):
    print(" [x] Получено %r" % body)

channel.basic_consume(callback,
                      queue='text',
                      no_ack=True)

print(' [*] Ожидания сообщений')
channel.start_consuming()