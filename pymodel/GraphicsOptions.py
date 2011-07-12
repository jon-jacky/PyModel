"""
Options and arguments for PyModel Graphics
"""

from optparse import OptionParser

usage = """pmg.py [options] fsm

PyModel Graphics. The single argument fsm is one finite state machine
(FSM) module name (without the .py suffix).  The FSM is typically
produced by the PyModel Analyzer, pma.py.  From the FSM, pmg generates
a file of commands in the dot graph-drawing language.  This .dot file
can then be processed by the dot program in the Graphviz package from
www.graphviz.org.  Use the PyModel commands dotps, dotpdf, or dotsvg to run dot
and produce PostScript, PDF, or SVG, respectively. SVG files can be viewed
in a web browser.

Control clutter in the graph with the -l --transitionLabels option:
-l action shows the action name, arguments, and return value,
-l name shows only the action name, and -l none shows no labels.

In the generated graphics, the initial state is gray.  Accepting
states have a double border.  Unexplored or incompletely explored
states are orange (these may have outgoing transitions that are
not shown). Terminal states (with no outgoing transitions) that are
accepting states are green.  Terminal states that are not accepting
states are yellow; runs that end in these states are considered
failures.

In the browser, hover the pointer over a state to display a tooltip
that shows the state variables and their values.  Place the point of
the pointer over any pixel on a transition vector to display a tooltip
that shows the transition.
"""

parser = OptionParser(usage=usage)

def parse_args():
    parser.add_option('-o', '--output', type='string', default='',
                  help = 'Output file name (not including .dot), default is <fsm argument>')
    parser.add_option('-l', '--transitionLabels', type='string', 
                      default='action',
                      help = 'Transition labels: action, name, or none, default is action')
    parser.add_option('-x', '--noStateTooltip', action="store_true", dest="noStateTooltip", 
                    help = 'Omit tooltips from state bubbles (to work around dot svg problem)')
    return parser.parse_args()

def print_help():
    parser.print_help()
