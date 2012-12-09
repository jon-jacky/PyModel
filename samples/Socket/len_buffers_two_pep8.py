"""pymodel config"""

import Socket

def len_buffers_two():
    return len(Socket.buffers) <= 2

Socket.state_filter = len_buffers_two
