cases = [
    ('pmt.py -s 2 -n 30 populations, first without state filter',
     'pmt.py -s 2 -n 30 populations'),

    ('pmt.py -s 2 -n 30 populations filter3, state filter limits population to 3',
     'pmt.py -s 2 -n 30 populations filter3'),

    ('pmt.py -s 2 -n 30 populations filter3_lc, BUG state filter spelled in lowercase has no effect',
     'pmt.py -s 2 -n 30 populations filter3_lc')
]
