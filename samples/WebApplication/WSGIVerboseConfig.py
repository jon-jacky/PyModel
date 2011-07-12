"""
Alternate site for web application, in case you don't have it on localhost.
Please be courteous, do not load this site too much!
"""

site = 'http://localhost:8000/'

path = ''
webAppPage = 'doStuff.php'
logoutPage = 'logout.php'

webAppUrl = site + path + webAppPage
logoutUrl = site + path + logoutPage

print 'webAppUrl %s' % webAppUrl # debug

debuglevel = 1  # 1: print HTTP headers, 0: don't print
# show_page = True 
