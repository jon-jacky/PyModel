The WebApplication sample includes a test harness (Stepper.py) to
connect it to an implementation.  The module test_stepper invokes
tests that use the harness and run the implementation.

The implementation is a small PHP web application.  It is not included
in PyModel; it is with one of the samples at
http://www.codeplex.com/NModel.  The stepper is configured to attempt
to connect to an instance running on localhost.  Alternatively, there
is an instance running (in Estonia!) at

 http://www.cc.ioc.ee/~juhan/nmodel/webapplication/php/doStuff.php

If you want to run tests on that instance, copy IocConfig.py to Config.py.
Please be courteous, do not load this site too much!

There is an deliberate error in the implementation: it does not retain
data across login sessions.  So, the test case in TestIntSuccess
succeeds but TestIntFailure fails.

