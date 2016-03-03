#port knocking script for KPMG CTF
#admin@theprohack.com
#I know the code is ugly but it works.
from scapy.all import *
#suppress output
conf.verb = 0
# Knock on every port
ip=IP(dst="119.9.109.73")
SYN = ip/TCP(sport=1337, dport=7000, flags="S", window=8192);
send(SYN) ;	print "KNOCK"
SYN= ip/UDP(sport=1337,dport=8000)
send(SYN); print "KNOCK"
SYN = ip/TCP(sport=1337, dport=9000, flags="S", window=8192);
send(SYN) ;	print "KNOCK"
SYN = ip/TCP(sport=1337, dport=5341, flags="S", window=8192);
send(SYN) ;	print "KNOCK"
# Use NMAP for scanning for open ports
print "Check if port is open : "
subprocess.call("nmap -p 5341 119.9.109.73", shell=True)
