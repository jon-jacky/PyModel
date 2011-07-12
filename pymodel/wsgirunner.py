#!/usr/bin/env python
"""
Simple web server for WSGI applications
using only Python standard libraries
"""

import sys
from wsgiref import simple_server
from optparse import OptionParser

usage = """python wsgirunner.py [options] arg

where arg is the name of a Python module arg.py
which contains a WSGI-compliant web application.
For example:

  python wsgirunner.py -p 8080 wsgidemo

If wsgirunner.py is in a directory that is on the
execution path, this can be shortened to 

  wsgirunner.py -p 8080 wsgidemo

"""

parser = OptionParser(usage=usage)

def parse_args():
  parser.add_option('-p', '--port', type='int', default=8000,
                  help='Port where server listens, default 8000')
  return parser.parse_args()

def print_help():
  parser.print_help()  # must have at least one arg, not optional
    
def main():
    (options, args) = parse_args()
    if not args:
        print_help()
        exit()
    app_module = args[0]
    app = __import__(app_module)
    application = app.application
    print "Running %s - point your browser at http://localhost:%s/" \
        % (app_module, options.port)
    httpd = simple_server.WSGIServer(('', options.port), 
                                     simple_server.WSGIRequestHandler)
    httpd.set_app(application)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
