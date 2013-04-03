cases = [
    ('pmt.py -s 1 -n 20 populations, use seed so same run each time',
     'pmt.py -s 1 -n 20 populations'),

    ('pmt.py -s 2 -n 6 populations, use seed so same run each time',
     'pmt.py -s 2 -n 6 -r 3 populations') 
]
