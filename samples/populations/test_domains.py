cases = [
    ('pmt.py -s 1 -n 20 populations, first with domains in defined model',
     'pmt.py -s 1 -n 20 populations'),

    ('pmt.py -s 2 -n 20 populations domains9, rebind domains in config file',
     'pmt.py -s 2 -n 20 populations domains9'),

    ('pmt.py -s 2 -n 20 domains9 populations, put config file first in args',
     'pmt.py -s 2 -n 20 domains9 populations')
]
