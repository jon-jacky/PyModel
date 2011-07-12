"""
pymodel configuration: rebind WebModel StateFilter
"""

import WebModel

def OneUserLoggedIn():
    return (WebModel.usersLoggedIn == [] 
            or WebModel.usersLoggedIn == [ 'VinniPuhh' ])

WebModel.StateFilter = OneUserLoggedIn
