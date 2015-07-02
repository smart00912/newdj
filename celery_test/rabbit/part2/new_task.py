__author__ = 'sean'
import sys,pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
# enable durable
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
# exchange='' means we are using default exchange
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message+"normal")
print " [x] Sent %r" % (message,)

channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message+"durable",
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
	                      # mode =2 tells RabbitMQ to save the message to disk in case it crashed
                      ))

connection.close()
