cases = [
    ('Push is observable here so no actions are enabled in the initial state',
     'pmt.py -n 10 -s 1 Stack Observables'),

    ('Accepts Push(3) but not Pop(3) because here Push is observable, Pop controllable',
     'pmt.py -n 10 -s 1 Stack Observables Scenarios'),

    ('Accepts both Push(3) and Pop(3) because here both are observable, still doesnt accept out-of-order Pop.',
     'pmt.py -n 10 -s 1 Stack AllObservables Scenarios'),
    ]
