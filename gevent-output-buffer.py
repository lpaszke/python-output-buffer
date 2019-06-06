# Copyright (c) 2019, Łukasz Paszke. All rights reserved. see README for details.

import sys

try:
    import gevent
except ImportError:
    print 'Please install gevent and its dependencies'
    sys.exit(1)

from gevent.queue import Queue, Empty
import socket

class GEventOutputBuffer(OutputBuffer):
    
    def __init__(self):
        
    
    def spawn_buffer_thread(spawn_function):
        gevent.spawn(spawn_function)
        
    def join_elements(elements_list)
        joined_elements = ''
        for element in elements_list
            joined_elements = joined_elements + element
        
    def send_joined_elements(joined_elements)
        
