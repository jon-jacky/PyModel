"""
Web application to test with PyModel WebApplication sample

This is a WSGI-compliant application.  Its behavior is similar to
Juhan Ernits' sample application in PHP at http://nmodel.codeplex.com/

To run this web application:

 wsgirunner webapp  # runs on port 8000 on localhost

or 

 wsgirunner -p 8080 webapp  # -p option sets port number on localhost

"""

import pprint
import urllib.parse

# page templates appear at the end of this file

# configuration
password = { 'user1':'123', 'user2':'234' }

# data state
integers = dict() # user to int
strings = dict() # user to str
sessions = dict() # cookie to user, assume each user has at most one session
next_cookie = 0 

def application(environ, start_response):
    global next_cookie

    # print environ_template % pprint.pformat(environ) # DEBUG, voluminous!

    response_headers = [] # add headers below
    cookie = environ.get('HTTP_COOKIE') # might be None

    # show login page
    if (environ['PATH_INFO'] == '/webapp.py' 
        and environ['REQUEST_METHOD'] == 'GET' 
        and cookie not in sessions): # cookie might be None
        response_body = login_page
        response_headers += [
            ('Set-Cookie','PYSESSID=%s; path=/' % next_cookie)]
        next_cookie += 1
        status = '200 OK'
        
    # log in, if successful show data form page
    elif (environ['PATH_INFO'] == '/webapp.py' 
          and environ['REQUEST_METHOD'] == 'POST'):
        wd = environ['wsgi.input']
        method = environ['REQUEST_METHOD']
        length = int(environ['CONTENT_LENGTH'])
        request_body = wd.read(length)
        vars = urllib.parse.parse_qs(request_body)
        user = vars['username'][0] # vars[x] are lists, get first item
        passwd = vars['password'][0]
        if user in password and password[user] == passwd:
            sessions[cookie] = user
            if not user in strings:
                strings[user] = ''
            # CORRECT CODE comented out
            # if not user in integers:
            #   integers[user] = 0
            # BUG follows, should be guarded by if ... like strings 
            integers[user] = 0 # BUG, always overwrites data from last session
            # PHP version sends redirect back to doStuff instead of this response_body
            #response_body = dostuff_template % (integers[user], 
            #                                   strings[user])
            response_headers += [('Location','webapp.py')]
            status = "302 Found"
            response_body = ''
        else:
            response_body = login_failure_page
            status = '200 OK'
            
    # submit data in form page
    elif (environ['PATH_INFO'] == '/webapp.py' 
          and environ['REQUEST_METHOD'] == 'GET' 
          and cookie in sessions):
        user = sessions[cookie]
        vars = urllib.parse.parse_qs(environ['QUERY_STRING'])
        if 'num' in vars:
            integers[user] = str(vars['num'][0]) # vars[x] are lists, 1st item
        if 'str' in vars:
            strings[user] = vars['str'][0]                              
        response_body = dostuff_template % (integers[user], 
                                            strings[user])
        status = '200 OK'

    # log out
    elif environ['PATH_INFO'] == '/logout.py':
        if cookie in sessions:
            del sessions[cookie]
        response_body = '' # blank page, like original NModel version
        status = '200 OK'
        pass
    
    # unknown page
    elif environ['PATH_INFO'] not in ('/webapp.py', '/logout.py'):
        response_body = p404_page        
        status = '404 Not Found'

    # nonsense: doStuff REQUEST_METHOD not GET or POST, or ... ?
    else:
        raise ValueError # send 500 Server Error

    # response
    response_headers += [('Content-Type', 'text/html'),
                         ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]


environ_template = """environ is 

%s

"""


p404_page = """<html>
<head>
<title>404 Not Found</title>
</head>
<body>
404 Not found
</body>
</html>
"""

login_page = """<html>
<head>
<title>LoginPage</title>
</head>
<body>
<form method="POST" action="webapp.py">
Username: <input type="text" name="username" size="20">
Password: <input type="password" name="password" size="20">
<input type="submit" value="Submit" name="login">
</form>
</body>
</html>
"""

login_failure_page = """
<head>
<title>Login Failure</title>
</head>
<body>
Incorrect login name or password. Please try again.
</body>
</html>
"""

# usage: dostuff_template % (integers[user], strings[user])
dostuff_template = """
<html>
<head>
<title>DoStuff</title>
</head>
<body>
Number: %s<br/>
String: %s
<form name="number" method="GET" action="webapp.py">
Number: <input type="text" name="num" size="2">
<input type="submit" value="Submit" name="inputNumber">
</form>
<form name="string" method="GET" action="webapp.py">
String: <input type="text" name="str" size="20">
<input type="submit" value="Submit" name="inputString">
</form>

<a href="logout.py">Log out</a>
</body>
</html>
"""

