import os, sys, time
os.system("clear")
os.system("figlet HPAS1369")
print "Author : Zero Hacker TH"
print "Group  : DedSec CyberTeam TH"
print
print "           [01]> Brute Frose              "
print "           [02]> DDos Attack              "
print "           [03]> NMap PortScanner         "
print "           [04]> System Vulnerabilities   "
print "           [05]> WordPrass Scan & Hacking "
print "           [06]> SQL Injation             "
print ".          [07]> Ubuntu Terminal          "
print
A = raw_input("HPAS1369 ==>> ")

if A == "1" or A == "01":
  os.system("python2 brute.py")

elif A == "2" or A == "02":
    os.system("figlet DDOS Attack")
    ip = raw_input("IP Address : ")
    port = raw_input("Port       : ")
    packet =raw_input("Packet     : ")
    os.system("python2 pntddos %s %s %s" % (ip, port, packet))

elif A == "3" or A == "03":
    os.system("figlet NMap Scan")
    host = raw_input("Host : ")
    os.system("nmap %s" % (host))