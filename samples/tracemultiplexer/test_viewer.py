"""
tracemultiplexer test - with graphics because this is a model for analysis
"""

cases = [
    ('Generate graph for synchronized threads that use tracelock',
     'pmv.py tracemultiplexer'),

    ('Generate graph for *un*synchronized threads that *ignore* tracelock',
     'pmv.py -m 300 unsynchronized tracemultiplexer'),
]

