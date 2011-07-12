"""pymodel config"""

from Socket import domains, send_call

# send_call arg is always 'a' so following recv will always process entire msg

domains.update({ send_call: {'msg':('a',)}})
