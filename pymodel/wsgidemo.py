"""
Minimal WSGI application demo

To run with wsgidemo.py:  python wsgirunner.py wsgidemo
"""

import pprint

body_template = """A WSGI application is a Python callable object named
'application' that is called by the web server on each HTTP request.
The application accepts two arguments: environ, a dictionary of
environment variables (keys) and their values, and start_response, a
callback used to send the HTTP response back to the server.

For more information see http://www.python.org/dev/peps/pep-0333/

In this application call, environ is 

%s
"""

def application(environ, start_response):
    response_body = body_template % pprint.pformat(environ)
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]
