"""
We need to put select in a separate module so "import select" works

To use this simulator, just put it in the same directory with your
PyModel socket steppers and rename it (or symlink it) to select.py.
The steppers will load this simulator instead of the standard library
module.
"""

from socket_simulator_s import select
