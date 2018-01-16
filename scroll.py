#!/usr/bin/env python

import time
import fourletterphat

print("""
Four Letter pHAT: scroll.py

Scrolls a message across the display.

Press Ctrl+C to exit.
""")
import fourletterphat as flp

message = "YARR PIRATES   "

while True:
    # Display the first four letters of the message
    flp.print_str(message[:4])

    # Take the first letter (position 0) of the message
    # and pop it onto the end of the string.
    message = message[1:] + message[0]

    flp.show()
    time.sleep(0.25)