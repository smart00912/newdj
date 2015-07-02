__author__ = 'sean'

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')


#  by not supplying the queue parameter to queue_declare,let server choose a random queue name 
# result = channel.queue_declare()

# disconnect the consumer the queue should be deleted. There's an exclusive flag
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# binding a queue with a a exchange
channel.queue_bind(exchange='logs',queue=queue_name)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r" % (body,)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

