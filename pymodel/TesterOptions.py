"""
Options and arguments for PyModel Tester
"""

from optparse import OptionParser

usage = """pmt.py [options] models  

models is a list of one or more module names (with no .py suffix).
Each module named in models must contain a model, that is: a model
program, an FSM, or a test suite.  In addition, a module named in
models can contain additional configuration information for a model
program.  Multiple models (model programs including configuration,
FSMs, and test suites) are composed into a product.  The tester
generates traces by executing the product, at random or guided by the
strategy option.  To just view the traces, omit the implementation
option.  To use pmt as an offline test generator, omit the
implementation option and use the output option to save the traces in
a test suite module.  To execute tests, provide the implementation
option.  To execute tests generated offline, provide that test suite
module as the single command argument.  To generate and execute tests
on-the-fly, provide one or more model programs and/or scenario FSMs as
command line arguments.  To save on-the-fly tests so they can be
reproduced later, use the output option to save them in a test suite
module."""

parser = OptionParser(usage=usage)

def parse_args():
  parser.add_option('-a', '--action', action="append", 
                  help='Action to execute, as many as needed, if no -a execute all actions')
  parser.add_option('-c', '--cleanupSteps', type="int", default=0, 
                  help = 'Maximum number of steps in the cleanup phase, default 0 for no cleanup')
  parser.add_option('-d', '--debug', action="store_true", dest="debug",
                  help = 'Run the main function in the debugger'),
  parser.add_option('-e', '--exclude', action="append", 
                  help='Action to exclude from execution, as many as needed')
  parser.add_option('-g', '--strategy', type='string', default='',
                  help = 'Strategy (module name), omit to use random strategy')
  parser.add_option('-i', '--iut', type='string', default='',
                  help = 'Implementation (stepper module name), omit to just run model')
  parser.add_option('-n', '--nsteps', type="int", default=0, 
                  help = 'Number of steps in a single test run before beginning cleanup phase, default 0 for no limit')
  parser.add_option('-o', '--output', type='string', default='',
                  help = 'Output test suite module name (with no .py suffix), no default (no output file if omitted)')
  parser.add_option('-q', '--quiet', action="store_true", dest="quiet", 
                    help = 'Omit arguments and return value from progress messages (to suppress printing very large buffers etc.)')
  parser.add_option('-r', '--nruns', type="int", default=1, 
                  help = 'Number of test runs, default 1, 0 for no limit')
  parser.add_option('-s', '--seed', type="int", default=0, 
                  help = 'Random seed, use any nonzero value to make runs reproducible')
  # timeout not yet working, comment out for now
  # parser.add_option('-t', '--timeout', type="int", default=0, 
  #              help = 'Number of seconds to wait for stepper to return from action before timing out and failing test, default 0 (no timeout, wait forever)')
  return parser.parse_args()

def print_help():
  parser.print_help()  # must have at least one arg, not optional
