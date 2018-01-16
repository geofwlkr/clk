#!/usr/bin/env python

import time
import fourletterphat as flp

print("""
Four Letter pHAT: demo.py

Displays a basic demo sequence.

Press Ctrl+C to exit.
""")


words = ["AHOY", "YARR", "GROG"]
spinner = ["|", "/", "-", "\\"]

while True:
    for w in words:
        flp.clear()
        flp.print_str(w)
        flp.show()
        time.sleep(1)

    for i in range(4):
        for s in spinner:
            # Take the single character from the spinner and repeat it 4 times
            # This is a little weird because: 2 * 4 = 8
            # But "|" * 4 = "||||"
            # And "/" * 4 = "////"
            # etc.
            s = s * 4

            # Display our new 4 character long spinner
            flp.clear()
            flp.print_str(s)
            flp.show()
            time.sleep(1 / 16.0)

    # Count up to 9999 in increments of 25
    for i in range(0, 10000, 25):
        flp.clear()
        flp.print_number_str(str(i))
        flp.show()
        time.sleep(1 / 10000.0)