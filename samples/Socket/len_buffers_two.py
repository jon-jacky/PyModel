"""pymodel config"""

import Socket

def len_buffers_two():
    return len(Socket.buffers) <= 2

Socket.StateFilter = len_buffers_two
