#!/usr/bin/env python

import fourletterphat as flp

print("""
Four Letter pHAT: glow.py

This example will glow a message at different speeds and durations.

Press Ctrl+C to exit.
""")

while True:
    flp.clear()
    flp.print_str("P1D4")
    flp.show()
    flp.glow(period=1, duration=4)

    flp.print_str("P4D8")
    flp.show()
    flp.glow(period=4, duration=8)