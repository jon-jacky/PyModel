"""
Test the -q --quiet option that omits arguments and results 
from pmt progress messages.
"""

cases = [
    ('Deliberate failure on 16-char message, show progress messages:',
     'pmt.py Msg16Fail -i Stepper'),

    ('Deliberate failure, quieter messages with -q option:',
     'pmt.py Msg16Fail -i Stepper -q')
]
