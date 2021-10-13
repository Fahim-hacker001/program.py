print("\033[92m")
import os
import sys
import urllib2
os.system("figlet Web Eye")
print("\033[91m")
print("Coded by: Fahim Abrar Niloy ")
print("\033[96m")
url = raw_input("Enter Website Link: ")
url.rstrip ( )
header = urllib2.urlopen (url) .info ( )
print(str (header) )
