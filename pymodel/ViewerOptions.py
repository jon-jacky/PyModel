"""
Options and arguments for PyModel Viewer
"""

from optparse import OptionParser

usage = """pmv [options] models  

PyModel Viewer.  A single program that invokes pma, pmg, and Graphviz
dot to to perform analysis, generate dot commands, and generate a file
of graphics in .svg, .pdf or another format.  The pmv program provides
brevity and convenience, so analysis and display can be accomplished
by a single command.  This program accepts all of the command line
options and arguments of both pma and pmg, and the -T option of dot
(to select the graphics format), then passes the options to the
appropriate program.

Options aemo are passed to pma, lxy are passed to pmg, T is passed to dot."""

parser = OptionParser(usage=usage)

def parse_args():

  # options for pma from AnalyzerOptions
  parser.add_option('-a', '--action', action="append", 
                  help='Action to include in generated FSM, as many as needed, if no -a include all actions')
  parser.add_option('-e', '--exclude', action="append", 
                  help='Action to exclude from generated FSM, as many as needed')
  parser.add_option('-m', '--maxTransitions', type="int", default=100, 
                  help = 'Maximum number of transitions to include in the generated FSM, default 100')
  parser.add_option('-o', '--output', type='string', default='',
                  help = 'Output file basename (before the .foo suffix), default is <first argument>FSM')

  # options for pmg from GraphicsOptions
  # -o --output is already handled above
  parser.add_option('-l', '--transitionLabels', type='string', 
                      default='action',
                      help = 'Transition labels: action, name, or none, default is action')
  parser.add_option('-x', '--noStateTooltip', action="store_true", dest="noStateTooltip", 
                    help = 'Omit tooltips from state bubbles (to work around dot svg problem)')
  parser.add_option('-y', '--noTransitionTooltip', action="store_true", dest="noTransitionTooltip", 
                    help = 'Omit tooltips from transition arrows')

  # options from graphviz dot
  parser.add_option ('-T', '--fileType', type='string', default='svg',
                     help = 'Graphics file type (format), default svg')

  return parser.parse_args()

def print_help():
  parser.print_help()  # must have at least one arg, not optional
