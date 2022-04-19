#!/usr/bin/env python
import subprocess
#import time
import optparse
import re

parse = optparse.OptionParser()
parse.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parse.add_option("-m","--mac", dest="new_mac", help="New MAC address")
(options, arguments) = parse.parse_args()

interface = options.interface
new_mac = options.new_mac


#for old_mac
result = subprocess.check_output(["ifconfig", options.interface])
old_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)
print(old_mac.group(0))

#using call("command",shell=True) has some security flaw

print(f"[*] Changing MAC address for {interface} to {new_mac} (old_mac)\n")
#subprocess.call(f"sudo ifconfig {interface} down",shell=True)
#subprocess.call(["sudo","ifconfig",interface,"down",])
#time.sleep(6)
#subprocess.call(f"sudo ifconfig {interface} hw ether {new_mac} ",shell=True)
#subprocess.call(["sudo","ifconfig",interface,"hw","ether",new_mac])
#time.sleep(2)
#subprocess.call(f"sudo ifconfig {interface} up",shell=True)
#subprocess.call(["sudo","ifconfig",interface,"up"])
print(f"[+] Successfully MAC address {new_mac}")
