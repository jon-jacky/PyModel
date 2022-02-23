#!/usr/bin/env python
"""
PyModel Analyzer - generate FSM from product model program
"""

from pymodel import Analyzer
from pymodel import AnalyzerOptions
from pymodel.ProductModelProgram import ProductModelProgram

def main():
    (options, args) = AnalyzerOptions.parse_args()
    if not args:
        AnalyzerOptions.print_help()
        exit()
    else:
        mp = ProductModelProgram(options, args)
        Analyzer.explore(mp, options.maxTransitions)
        print('%s states, %s transitions, %s accepting states, %s unsafe states' % \
            (len(Analyzer.states),len(Analyzer.graph),len(Analyzer.accepting),len(Analyzer.unsafe)))
        mname = options.output if options.output else '%sFSM' % args[0]
        Analyzer.save(mname)

if __name__ == '__main__':
    main ()
