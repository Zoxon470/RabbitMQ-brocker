import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='text')

channel.basic_publish(exchange='',
                      routing_key='text',
                      body='Simple text for testing program')
print(" [x] Сообщение отправлено! ")
connection.close()