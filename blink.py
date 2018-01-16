#!/usr/bin/env python

import time
import fourletterphat as flp

print("""
Four Letter pHAT: blink.py

Demonstrate the display blinking at
the three available speeds.

Press Ctrl+C to exit.
""")

flp.clear()
flp.print_str("BLNK")
flp.show()

# Display each blinkt speed for 4 seconds
for blink_speed in [
        flp.HT16K33_BLINK_HALFHZ,
        flp.HT16K33_BLINK_1HZ,
        flp.HT16K33_BLINK_2HZ]:
    flp.set_blink(blink_speed)
    time.sleep(4)

flp.set_blink(flp.HT16K33_BLINK_OFF)

flp.print_str("BOOM")
flp.show()
time.sleep(1)(10)