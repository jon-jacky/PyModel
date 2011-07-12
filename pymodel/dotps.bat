rem Generate .ps from .dot and display (can optionally suppress display)
rem %1 is basename of dot file (without .dot),any %2 suppresses display of .ps
dot -v -Tps -Gsize="8,10.5" -o %1.ps %1.dot
if "%2" == "" start %1.ps

