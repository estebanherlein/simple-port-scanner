from socket import *
import sys
import time
from datetime import datetime


def scan_host(targethost, targetport, r_code=1):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        code = s.connect_ex((targethost, targetport))
        if code == 0:
            r_code = code
        s.close()
    finally:
        return r_code


try:
    host = input("[*] Enter target Host address: ")
    min_port = int(input("Enter starting port: "))
    max_port = int(input("Enter ending port: "))
except KeyboardInterrupt:
    print("\n\n[*] User requested interruption")
    sys.exit(1)

hostip = gethostbyname(host)
print("\n[*] Host %s IP: %s" % (host, hostip))
print("[*] Scan started at %s \n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

for port in range(min_port, max_port):
    try:
        response = scan_host(hostip, port)
        if response == 0:
            print("[*] Port %d seems open" % port)
    except:
        pass


stop_time = datetime.now()
total_time_duration = stop_time - start_time
print("\n[*] Scan finished at %s" % (time.strftime("%H:%M:%S")))
print("[*] Scan took %s" % total_time_duration)
