"""
WebApplication stepper (test harness)
"""

import re
import urllib
import urllib2
import cookielib

# Default stepper configuration for 
# webapp.py running on localhost at port 8080

site = 'http://localhost:8080/'
path = ''
webAppPage = 'webapp.py'
logoutPage = 'logout.py'

webAppUrl = site + path + webAppPage
logoutUrl = site + path + logoutPage

# user in model : user in implementation

users = { "OleBrumm":"user1", "VinniPuhh":"user2" }
passwords = { "user1":"123", "user2":"234" }
wrongPassword = "000"

debuglevel = 0     # for debug_handler 1: print HTTP headers, 0: don't print
show_page = False

# Optionally rebind configuration. If no Config module found, retain defaults.

try:
  from Config import *
except ImportError:
  pass 

print 'webAppUrl: %s' % webAppUrl # show which config file (if any) 

# handlers that are the same for all users

redirect_handler= urllib2.HTTPRedirectHandler()
debug_handler = urllib2.HTTPHandler(debuglevel=debuglevel)

# handlers that are different for each user are part of the session state

class Session(object):
  """
  One user's session state: cookies and handlers
  """
  def __init__(self):
    self.cookies = cookielib.CookieJar()
    self.cookie_handler = urllib2.HTTPCookieProcessor(self.cookies)
    self.opener = urllib2.build_opener(self.cookie_handler,
                                       redirect_handler,debug_handler)

session = dict() # each user's Session

# helpers, determine test results by scraping the page

# like in NModel WebApplication WebTestHelper
def loginFailed(page):
  return (page.find('Incorrect login') > -1)

# not in NModel WebApplication, it has no positive check for login success
def loginSuccess(page):
  return (page.find('DoStuff') > -1)

# similar to NModel WebApplication WebTestHelper
intPattern = re.compile(r'Number: (\d+)')

def intContents(page):
  m = intPattern.search(page)
  if m:
    return int(m.group(1))

# stepper core

def TestAction(aname, args, modelResult):
  """
  To indicate success, no return statement (or return None)
  To indicate failure, return string that explains failure
  Test runner also treats unhandled exceptions as failures
  """

  global session

  if aname == 'Initialize':
    session = dict() # clear out cookies/session IDs from previous session

  elif aname == 'Login':
    user = users[args[0]]
    if user not in session:
      session[user] = Session()
    password = passwords[user] if args[1] == 'Correct' else wrongPassword
    postArgs = urllib.urlencode({'username':user, 'password':password})
    # GET login page
    page = session[user].opener.open(webAppUrl).read()
    if show_page:
      print page
    # POST username, password
    page = session[user].opener.open(webAppUrl, postArgs).read()
    if show_page:
      print page
    # Check conformance, reproduce NModel WebApplication Stepper logic:
    # check for login failed message, no check for positive indication of login
    result = 'Success'
    if loginFailed(page):
      result = 'Failure'
    if result != modelResult:
      return 'received Login %s, expected %s' % (result, modelResult)

  elif aname == 'Logout':
    user = users[args[0]]
    page = session[user].opener.open(logoutUrl).read()
    del session[user] # clear out cookie/session ID
    if show_page:
      print page

  elif aname == 'UpdateInt':
    user = users[args[0]]
    numArg = urllib.urlencode({'num':args[1]})
    page = session[user].opener.open("%s?%s" % (webAppUrl,numArg)).read()
    if show_page:
      print page

  elif aname == 'ReadInt':
    user = users[args[0]]
    page = session[user].opener.open(webAppUrl).read()
    if show_page:
      print page
    numInPage = intContents(page)    
    if numInPage != modelResult:  # check conformance
      return 'found %s in page, expected %s' % (numInPage, modelResult)
    else:
      return None
  else:
    raise NotImplementedError, 'action %s not handled by stepper' % aname


def Reset():
  global session
  session.clear()
