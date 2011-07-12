#!/usr/bin/env python
"""
PyModel Graphics - generate graphics from pymodel FSM
"""

import GraphicsOptions
from Dot import dotfile

def main():
    (options, args) = GraphicsOptions.parse_args()
    if not args or len(args) > 2: # args must include one FSM module
        GraphicsOptions.print_help()
        exit()
    else:
        fsm = __import__(args[0])
        fbasename = options.output if options.output else args[0]
        fname = '%s.dot' % fbasename
        dotfile(fname, fsm, options.transitionLabels, options.noStateTooltip)

if __name__ == '__main__':
    main ()
