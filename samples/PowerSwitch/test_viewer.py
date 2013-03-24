"""
Like test_graphics, except just uses one pvm command 
instead of three: pma, pmg, dot. 
Output files have the same names and should have the same contents as 
in test_graphics output files saved in fsmpy/ and svg/
"""

cases = [
    ('Generate FSM from PowerSwitch model program',
     'pmv -T svg PowerSwitch'),

    ('Generate graphics from SpeedControl (already an FSM)',
     'pmv SpeedControl -o SpeedControl'), # -T svg is the default
                                          # -o for SpeedControl.svg not ...FSM.svg

    ('Generate FSM from composition of PowerSwitch and SpeedControl, show interleaving',
     'pmv -T svg SpeedControl PowerSwitch -o PowerSpeed'),

    # Now you can display PowerSwitchFSM.svg, SpeedControl.svg and PowerSpeed.svg 
    # in three browser tabs
]
    
