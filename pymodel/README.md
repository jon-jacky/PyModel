
pymodel directory
=================

This directory contains the Python modules for PyModel.

To use PyModel, this directory must be on your Python path.
The usual way to achieve this is to add it to your *PYTHONPATH*.  Or, its
contents must be installed in some directory that is on your Python
path.  See *pymodel_paths* in the *bin* directory.

This directory does not need not be on your execution *PATH*, because
its modules are usually invoked through the commands in the PyModel
*bin* directory.

The Python modules are:

- *pma*, *pmg*, *pmt*, *pmv*: the main modules for the four main
   PyModel programs.  For details, see *commands.txt* in the *notes* 
   directory, or print their built-in help by typing *pma -h* etc.

- *trun*: runs test scripts, including sample demonstrations.  See
   *test.txt* in the *notes* directory.

- *wsgirunner*: runs WSGI-compliant web applications on *localhost*,
  such as *webapp* in the *WebApplication* sample, or *wsgidemo* here.
  
- *wsgidemo*: a sample web application to run with *wsgirunner*

All the other modules here are used by *pma*, *pmg*, *pmt*, and *pmv*.


Revised Apr 2013
