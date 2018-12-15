from socket import *
import sys
import time
from datetime import datetime
from threading import Thread

threads = []
timeout = 5

try:
    host = input("[*] Enter target Host address: ")
    hostip = gethostbyname(host)
    min_port = int(input("Enter starting port: "))
    max_port = int(input("Enter ending port: "))
except KeyboardInterrupt:
    print("\n\n[*] User requested interruption")
    sys.exit(1)


def scan_host(targetport):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((hostip, targetport))
        if result == 0:
            response = s.recv(1024)
            print("[*] Port %d seems open" % targetport)
            try:
                print(response.decode('utf-8', 'ignore'))
            except:
                pass
        s.close()
    except:
        print("Something went wrong when scouting port %d" % targetport)


print("\n[*] Host %s IP: %s" % (host, hostip))
print("[*] Scan started at %s \n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

for i in range(min_port, max_port+1):
    thread = Thread(target=scan_host, args=(i,))
    threads.append(thread)
    thread.start()

[x.join() for x in threads]


stop_time = datetime.now()
total_time_duration = stop_time - start_time
print("\n[*] Scan finished at %s" % (time.strftime("%H:%M:%S")))
print("[*] Scan took %s" % total_time_duration)
