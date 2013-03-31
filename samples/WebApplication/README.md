
WebApplication
==============

This sample contains *WebModel*, a model for a web application,
*webapp*, an actual web application implementation (in Python), and
*Stepper*, a stepper that allows the tester *pmt* to use the model to
drive the web application.

The web application has a bug -- it doesn't conform to the
model.

Start the web application on localhost at port 8000: *wsgirunner webapp*.
Use the *-p* option to use a different port: *wsgirunner -p 8080 webapp*
To stop the web application, type ^C in the terminal window where you
started it, or close the window.

To see the web application running, point a browser at
*http://localhost:8000/webapp.py* (or whatever port you chose).  At
*Username:* enter *user1* (or *user2*), at *Password:* enter *123* (or
*234*), then click *Submit*.  

On successful login, the web application displays a data page that
shows a number, a string, and forms to enter a new value for each.  Enter
and submit some new values; the page updates to show the most recent
entries.  Select the *Log out* link, the application shows a blank page.

Enter the original *webapp.py* URL into the browser to log in as the
same user again.  The data page appears, showing the string you
entered during the last session, but the number zero.  This is the
bug: the web application is supposed to store both the string and
number entered by each user, and persist them from one login session
to the next, but it fails to store the number.

*Stepper* is a web client.  It simulates a browser, sending HTTP
requests to the web application.  It uses the *urllib*, *urllib2*, and
*cookielib* modules from the Python standard library.

By default, *Stepper* accesses *http://localhost:8000/webapp.py*.
Alternatively, *Stepper* can use an optional *Config* module to select
a different URL, or to select other options, such as printing out
incoming HTTP requests.  The sample includes several configuration
modules: *WSGIVerboseConfig* etc.  To use one, copy it (or symlink it)
to *Config.py*.

The only test script that uses *Stepper* is *test_stepper*.  To run 
this test, you must first start the web application.

The rest of the test scripts only execute the model, so they do not
need the web application to be running: *test*,
*test_graphics*, and several others.

The modules are:

- *WebModel*: model program for the web application

- *webapp*: web application (implementation)

- *Stepper*: enables *pmt* to use *WebModel* (etc.) to drive *webapp*

- *WSGIVerboseConfig*, *wsgiconfig*, *PHPLocalConfig*,
  *local8080config*, *VerboseConfig*, *nmodelconfig*: 
  configuration modules for *Stepper* that select different URLs for the web
  application, or other options such as printing the HTTP headers.

- *OneUserDomain*: configuration for *WebModel*, limits *users* domain to one
   particular element

- *OneUserFilter*: configuration for *WebModel*, assigns *StateFilter*
  to allow only one particular logged in user

- *OneUserScenario*: scenario machine (FSM), compose with *WebModel*
  to allow only one particular user to log in and log out

- *OneUserNoIntScenario*: scenario machine (FSM), compose with *WebModel*
  to allow only one particular user to log in and log out *and*
  to suppress the *UpdateInt* and *ReadInt* actions

- *ScenarioLogin*: test suite, compose with *WebModel* to allow only
  one particular user to log in and log out

- *TestIntFailure*, *TestIntSuccess*, *TestIntSuccessNoNone*, 
  *TestIntTwoRuns*, *TestIntTwoUsers*, *TestIntWrong*, *TestIntWrongLogout*,
  *TestLoginFiveFailures*: test suites, use as offline tests

- *test*: use *pmt* to generate traces from *WebModel*, with many test
   cases that demonstrate various *pmt* options and the built-in
   *ActionNameCoverage* and *StateCoverage* strategies.  Also, one
   test case that executes the *TestIntTwoRuns* test suite.

- *test_offline*: uses the *pmt -o* option to generate an offline test suite.
  The *test_offline* module contains instructions for running the generated
  tests.

- *test_scenarios* - use *pmt* to generate traces from *ScenarioLogin*,
  *OneUserScenario*, and both composed with *WebModel*

- *test_stepper*: test script that invokes *pmt* using *Stepper*
   to drive the web application *webapp*.  The script includes test
   cases that do on-the-fly testing with *WebModel* and offline tests
   with *TestIntSuccess*, *TestIntFailure*, *TestIntTwoFailures*, 
   and *TestLoginFiveFailures*.  Test failures that indicate *ended in 
   non-accepting state* are expected; repeating those commands with the 
   *pmt -c 1* option will cause them to succeed.  Failures that indicate 
   *found 0 in page, expected 1* are caused by the persistence bug in
   the web application.  (This is the only sample that uses *Stepper* and 
   *webapp*.)

- *test_graphics*: generate graphs from *WebModel*, *OneUserDomain*,
  *OneUserScenario*, *OneUserFilter*, and *OneUserNoIntScenario*, alone 
  and in combination

- *test_validation* - generate graphs of the test suites *TestIntSuccess*
  and *TestIntWrong*, alone and composed with *WebModel*

- *test_no_composition*: generates graphs from the test suite
  *TestIntSuccess*, the FSM *OneUserScenario*, and the model program
  *WebModel*

- *test_composition*: generate graphs from *TestIntSuccess*, *TestIntWrong*,
  their composition *TestIntSuccess x TestIntWrong*, and the composition
  *TestIntSuccess x TestIntWrongLongout*

- *test_e_testsuite*: - generate graphs from *TestIntTwoRuns*,
   demonstrates the *pmv -e*, *-a*, and *-o* options

- *test_ls*: show you can run any program in a test script, not just
   PyModel programs

- *fsmpy*, *svg*: directories of output files from *test_graphics*
  or *test_viewer*

View the generated graphics files in a browser.  Hover the pointer
over any state bubble to see a tooltip that shows the state variables
in that state.

- *WebModelFSM*: graph generated by exploring *WebModel* alone,
  limited only by the *pma -m 50* option (to limit the number of
  transitions).  Exploration stopped at all the states colored orange.

- *OneUserScenario*, *OneUserNoIntScenario*: scenario machines (FSMs)
   for composing with *WebModel*

- *OneUserScenarioFSM*, *OneUserNoIntScenarioFSM*, *OneUserFilterFSM*,
  *OneUserDomainFSM*: graphs generated from *WebModel* combined with 
  other modules that restrict its behavior.

- *TestIntWrongLogoutFSM*, *TestIntWrongFSM*,
  *TestIntTwoRuns_NoLogout*, *TwoIntTwoRuns_Add*, *TestIntTwoRunsFSM*,
  *TestIntSuccessFSM*, *TestIntFailureFSM*: graphs of test
  suites including traces that are forbidden by the model.  They all
  reach their own accepting states, which are colored green.

- *TestWrongComposeFSM*, *TestSuccessComposeFSM*,
  *TestComposeLogoutFSM*, *TestIntComposeFSM*: graphs of tests
  suites composed with the model.  Each trace ends in the last state
  allowed by the model.  If this is not the last state in the trace
  from the test suite, it is colored yellow.  This indicates that the
  trace is not allowed by the model.  If the whole trace is allowed by
  the model, the last state is green.

Revised Mar 2013
