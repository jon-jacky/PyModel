"""
Marquee tests
"""

cases = [
    ('One run',
     'pmt.py Marquee -n 10'),

    ('Request two runs, but no Reset function, so only one run executes',
     'pmt.py Marquee -n 10 -r 2')
]
