#!/usr/bin/env python

import fourletterphat as flp



print("""
Four Letter pHAT: scroll_print.py

This example will scroll a message at different speeds.

Press Ctrl+C to exit.
""")

while True:
    flp.clear()
    flp.scroll_print("DEFAULT SCROLLING SPEED")
    flp.scroll_print("1 SECOND PERIOD SCROLLING", 1)
    flp.scroll_print("1/10 SECOND PERIOD SCROLLING", 0.1)