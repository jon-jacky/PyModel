"""
Experiment with code for WebApplication stepper
"""

import re
import urllib
import urllib2
import cookielib

# Scrape page contents

def loginFailed(page):
  return (page.find('Incorrect login') > -1)

intPattern = re.compile(r'Number: (\d+)')

def intContents(page):
  m = intPattern.search(page)
  if m:
    return int(m.group(1))
  else: 
    return None

def main():

  # Configure.  Web application in this sample requires cookies, redirect
  cookies = cookielib.CookieJar()
  cookie_handler = urllib2.HTTPCookieProcessor(cookies)
  redirect_handler= urllib2.HTTPRedirectHandler()
  debug_handler = urllib2.HTTPHandler(debuglevel=1) # print headers on console
  opener = urllib2.build_opener(cookie_handler,redirect_handler,debug_handler)

  # Constants
  site = 'http://localhost/'
  path = 'nmodel/webapplication/php/'
  webAppPage = 'doStuff.php'  # Shouldn't this be called webAppPage, ...Url -?
  logoutPage = 'logout.php'

  webAppUrl  = site + path + webAppPage
  logoutUrl  = site + path + logoutPage

  print 'GET to show login page'
  print opener.open(webAppUrl).read()

  print 'POST to login with sample username and password, pass separate args for POST'
  args = urllib.urlencode({'username':'user1', 'password':'123'})
  page = opener.open(webAppUrl, args).read()  # should show successful login
  print page
  if loginFailed(page):
    print 'Login FAILED'

  print 'GET with arg in URL to UpdateInt on server'
  num = 99
  wrongNum = 'xx'
  numArg = urllib.urlencode({'num':num})
  print opener.open("%s?%s" % (webAppUrl,numArg)).read()

  print 'GET to retrieve page with integer'
  page = opener.open(webAppUrl).read()
  print page
  print '%s found in page, expected %s' % (intContents(page), num)
  print

  print 'GET to logout'
  print opener.open(logoutUrl).read()

  print 'GET to show login page -- again'
  print opener.open(webAppUrl).read()

  print 'POST to login with username and WRONG password'
  args = urllib.urlencode({'username':'user1', 'password':'321'}) # wrong pass
  page = opener.open(webAppUrl, args).read()  # should show login fail
  print page
  if loginFailed(page):
    print 'Login FAILED'

  # No logout this time - we're not logged in

if __name__ == '__main__':
  main()
