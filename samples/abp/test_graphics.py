"""
ABP analyzer and graphics tests
"""

cases = [
    ('Run Pymodel Graphics to generate dot file from FSM model, no need use pma',
     'pmg.py ABP'),

    ('Generate SVG file from dot',
     'dotsvg ABP'),

    # Now display ABP.dot in browser

    ('Run PyModel Analyzer to generate FSM from original FSM, should be the same',
     'pma.py ABP'),

    ('Run PyModel Graphics to generate a file of graphics commands from new FSM',
     'pmg.py ABPFSM'),

    ('Generate an svg file from the graphics commands',
     'dotsvg ABPFSM'),

    # Now display ABPFSM.svg in browser, should look the same as ABP.svg
]
