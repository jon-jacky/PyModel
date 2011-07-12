rem generate pdf of just the contents of the bounding box of ps from dot
rem %1 is basename of dot file (without .dot),x arg below suppresses ps display
call dotps %1 x
ps2epsi %1.ps %1.eps
epstopdf %1.eps
