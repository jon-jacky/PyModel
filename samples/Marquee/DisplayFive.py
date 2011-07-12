"""pymodel config"""

import Marquee

Marquee.actions = (Marquee.Load, Marquee.Shift)
Marquee.domains = { Marquee.Load: { 'pattern': ('Bye  '*5,) }}
