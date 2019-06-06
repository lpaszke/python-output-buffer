# Copyright (c) 2019, Łukasz Paszke. All rights reserved. see README for details.

try:
    import gevent
except ImportError:
    print 'Please install gevent and its dependencies'

class GEventOutputBuffer(OutputBuffer):
    def spawn_buffer_thread(spawn_function):
        gevent.spawn(spawn_function)
        
