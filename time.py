#!/usr/bin/env python

import time
import fourletterphat as flp

#print(""" Four Letter pHAT: clock.py
#
#This example will display a simple HH/MM clock, with a blinking decimal point to
#indicate seconds.
#
#Press Ctrl+C to exit. """)

#if 4 <= day <= 20 or 24 <= day <= 30:
#    suffix = "th"
#else:
#    suffix = ["st", "nd", "rd"][day % 10 - 1]


def full_string():
	
	day = int(time.strftime("%d"))

	if 4 <= day <= 20 or 24 <= day <= 30:
		suffix = "th"
	else:
		suffix = ["st", "nd", "rd"][day % 10 - 1]



	fs = time.strftime("%A") + "    " + time.strftime("%B") + "    " + time.strftime("%d") + suffix+ "    " + time.strftime("%Y") + "    " +  time.strftime("%H%M")
	return fs.upper()

def time_string():
	return time.strftime("%H%M")







while True:
	flp.clear()
	try:
		if (time.strftime("%S") == "00"):
			ctr = 1
			str_time = full_string()

			flp.scroll_print(str_time,0.5)
		else:

			str_time = time_string()
			flp.print_number_str(str_time)
			flp.set_decimal(1, int(time.time() % 2))
			flp.show()
			time.sleep(0.1)
	except:
		print('Error at{}'.format(full_string))# if exception 1 raised do this



