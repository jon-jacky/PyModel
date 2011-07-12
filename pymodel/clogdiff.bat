@echo off
rem Run command %1 with arg %2, save output in log, compare to reference log
%1 %2 > %2.log
fc %2.log %2.ref      
