"""
Options and arguments for PyModel Analyzer
"""

from optparse import OptionParser

usage = """pma.py [options] models  

PyModel Analyzer. models is a list of one or more module names (with
no .py suffix).  Each module named in models must contain a model,
that is: a model program, an FSM, or a test suite.  In addition, a
module named in models can contain additional configuration information
for a model program.  Multiple models (model programs including
configuration, FSMs, and test suites) are composed into a product.
The analyzer generates a finite state machine from the product and
writes an FSM module that includes the generated FSM, the explored
states, and other results of the analysis.  The FSM module contents
can be displayed using the PyModel Graphics program, pmg.py."""

parser = OptionParser(usage=usage)

def parse_args():
  parser.add_option('-a', '--action', action="append", 
                  help='Action to include in generated FSM, as many as needed, if no -a include all actions')
  parser.add_option('-e', '--exclude', action="append", 
                  help='Action to exclude from generated FSM, as many as needed')
  parser.add_option('-m', '--maxTransitions', type="int", default=100, 
                  help = 'Maximum number of transitions to include in the generated FSM, default 100')
  parser.add_option('-o', '--output', type='string', default='',
                  help = 'Output module name (with no .py suffix), default is <first argument>FSM')
  return parser.parse_args()

def print_help():
  parser.print_help()  # must have at least one arg, not optional
