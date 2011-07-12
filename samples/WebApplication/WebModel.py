"""
WebModel, loosely based on C# WebApplication sample at nmodel.codeplex.com
BUT this model is synchronous - Login is not split into start, finish actions
"""

### Model

# State, with initial values

mode = 'Initializing'  # can't call it 'state', that has special meaning
usersLoggedIn = list()
userToInt = dict()

# Actions and enabling conditions

def Initialize():
  global mode
  mode = 'Running'

def InitializeEnabled():
  return mode == 'Initializing'

def Login(user, password):
  global usersLoggedIn
  if (password == 'Correct'):
    usersLoggedIn.append(user)    
    return 'Success'
  else:
    return 'Failure'

def LoginEnabled(user, password):  # arg list must match Action
  return (mode == 'Running' and user not in usersLoggedIn)

def Logout(user):
  global usersLoggedIn
  usersLoggedIn.remove(user)

def LogoutEnabled(user):
  return (mode == 'Running' and user in usersLoggedIn)

def UpdateInt(user, number):
  global userToInt
  userToInt[user] = number

def UpdateIntEnabled(user, number):
  return (mode == 'Running' and user in usersLoggedIn)

def ReadInt(user):
  return userToInt.get(user, 0) # return default 0 if user not in dictionary

def ReadIntEnabled(user):
  return (mode == 'Running' and user in usersLoggedIn)

def Accepting():
  return not usersLoggedIn

### Metadata

state = ('mode', 'usersLoggedIn', 'userToInt')

actions = (Initialize, Login, Logout, UpdateInt, ReadInt)

enablers = { Initialize:(InitializeEnabled,), Login:(LoginEnabled,), 
             Logout:(LogoutEnabled,), UpdateInt:(UpdateIntEnabled,), 
             ReadInt:(ReadIntEnabled,) }

cleanup = (Logout,)

# default domains

users = ['VinniPuhh', 'OleBrumm']
passwords = ['Correct', 'Incorrect']
numbers = [ 1, 2 ]  # different from default 0

domains = { Login: {'user':users, 'password':passwords}, 
            Logout: {'user':users}, 
            UpdateInt: {'user':users, 'number':numbers},
            ReadInt: {'user':users} }

# needed for multiple test runs in one session

def Reset():  
  global mode, usersLoggedin, userToInt
  mode = 'Initializing'
  del usersLoggedIn[:]
  userToInt.clear()
