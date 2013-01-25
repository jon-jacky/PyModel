"""pymodel config"""

import msocket

msocket.observables = (msocket.send_call, msocket.send_return, 
                       msocket.recv_call, msocket.recv_return)
