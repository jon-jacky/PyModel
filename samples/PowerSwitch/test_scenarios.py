cases = [
    ('Scenarios module with four runs, by itself',
     'pmt Scenarios'),

    ('Scenarios module, compose with PowerSwitch model, last two runs not allowed',
     'pmt Scenarios PowerSwitch'),

    ('SpeedControl module, by itself',
     'pmt -n 2 -c 3 SpeedControl'),

    ('PowerSwitch module, compose with SpeedControl, no shared actions',
     'pmt -s 3 -n 10  -c 3 SpeedControl PowerSwitch')
    ]
