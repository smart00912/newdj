__author__ = 'sean'
# published log messages are going to be broadcast to all the receivers.
# here are a few exchange types available: direct, topic, headers and fanout.

import sys,pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='logs',
                      # not binding any queues,danout exchange will ignor all queues and will brocast to all workers
                      routing_key='',
                      body=message)
print " [x] Sent %r" % (message,)
connection.close()

# The messages will be lost if no queue is bound to the exchange yet, but that's okay for us; if no consumer is listening yet we can safely discard the message.








