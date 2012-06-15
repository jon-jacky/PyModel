"""pymodel config"""

from Socket import domains, send_call, send_return, recv_call, recv_return

n1 = 1
n2 = 2

a = 'a'*n1
aa = 'a'*n2

domains.update({ send_call: {'msg':(a, aa)},
                 send_return: {'n':(n1,n2)},
                 recv_call: {'bufsize':(n1,n2)}, 
                 recv_return:{'msg':('',a,aa)}})
