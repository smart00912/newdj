__author__ = 'sean'

import pika,time

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
# enable durable
channel.queue_declare(queue='task_queue', durable=True)


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep( body.count('.') )
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)
    
#  prefetch_count :don't dispatch a new message to a worker until it has processed and acknowledged the previous one
channel.basic_qos(prefetch_count=1)    
channel.basic_consume(callback,
                      queue='hello',
                      #no_ack=True
                      )
channel.basic_consume(callback,
                      queue='task_queue',
                      #no_ack=True
                      )

    
channel.start_consuming()