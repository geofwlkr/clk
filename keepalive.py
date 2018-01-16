
#NOTE!
#if psutil is not installed use the following
#sudo apt-get update
#sudo apt-get install python3-pip
#sudo pip install psutil



import psutil
import sys
from subprocess import Popen

for process in psutil.process_iter():
    if process.cmdline() == ['python3', '/home/pi/phat/time.py']:
        sys.exit('Process found: exiting.')

print('Process not found: starting it.')
Popen(['python3', '/home/pi/phat/time.py'])