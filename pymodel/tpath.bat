@echo off
rem Enable tools in this directory to import modules in current,test directories
set PYTHONPATH=.:..:test:tests:%PYTHONPATH%
