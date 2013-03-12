"""
test_analyze_msgsize - analyze msgsizes test suite by composing it with msocket model
"""

cases = [
    ("""Compose Socket model with msgsizes test suite and generate graphics.
Do not show argument lists and tooltips in graph because messages are so big.
""",
     'pmv -o msgsizesFSM msgsizes msocket all_observables -l name -xy'),
]
