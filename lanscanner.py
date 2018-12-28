import socket
from threading import Thread

threads = []
timeout = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("gmail.com", 80))
lan_ip, sock_port = s.getsockname()
print(lan_ip)
s.close()

octets = lan_ip.split('.')  # getting the octets


def scan_ip(variation):
    try:
        found = socket.gethostbyaddr('{}.{}.{}.{}'.format(octets[0], octets[1], octets[2], variation))
        print('[+] {}'.format(found))
    except:
        pass


for i in range(255):
    thread = Thread(target=scan_ip, args=(i,))
    threads.append(thread)
    thread.start()
