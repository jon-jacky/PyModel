cases = [
    ('pmt -s 1 -n 20 populations, first with domains in defined model',
     'pmt -s 1 -n 20 populations'),

    ('pmt -s 2 -n 20 populations domains9, rebind domains in config file',
     'pmt -s 2 -n 20 populations domains9'),

    ('pmt -s 2 -n 20 domains9 populations, put config file first in args',
     'pmt -s 2 -n 20 domains9 populations')
]
