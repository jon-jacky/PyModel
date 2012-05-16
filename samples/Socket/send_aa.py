"""pymodel config"""

from Socket import domains, send_call, recv_call, recv_return
from block import a, aa, n1, n2

domains.update({ send_call: {'msg':(a, aa)},
                 recv_call: {'bufsize':(n1,n2)}, 
                 recv_return:{'msg':('',a,aa)}})
