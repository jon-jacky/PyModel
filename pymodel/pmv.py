#!/usr/bin/env python
"""
PyModel Viewer - call pma, pmg, dot.  Handle all the command line options
"""

import os
import ViewerOptions

pma_keys = [ 'action', 'exclude', 'maxTransitions', 'output' ]
pmg_keys = [ 'transitionLabels', 'noStateTooltip', 'noTransitionTooltip' ]

def make_opts(keys, options):
    return ' '.join([('--%s %s' % (k,options.__dict__[k])) 
                     for k in keys if options.__dict__[k]])

def command(cmd):
    print cmd # DEBUG
    status = os.system(cmd)
    if status:
        print 'Failed: %s' % cmd  # status 0 means success

(options, args) = ViewerOptions.parse_args()
basename = options.__dict__['output'] if options.__dict__['output'] else '%sFSM' % args[0]
pma = 'pma.py ' + make_opts(pma_keys, options) + ' ' + ' '.join(args)
command(pma)
pmg = 'pmg.py ' + make_opts(pmg_keys, options) + ' %s' % basename
command(pmg)
dot = 'dot -T%(type)s -o %(name)s.%(type)s %(name)s.dot' % \
    {'type': options.__dict__['fileType'], 'name': basename}
command(dot)
