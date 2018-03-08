import socket
import time
from urlparse import urlparse

INFRASTRUCTURE_IP="...."
URL_LIST="urls-to-test"

with open(URL_LIST) as f:
    for line in f:
        the_url = line.rstrip()
        o = urlparse(the_url)
        domin = o.netloc
        path = o.path
        if path == '' or path == ' ':
            path = "/"
        try:
            print(b"GET " + str.encode(path) + " HTTP/1.1\r\nHost: " + str.encode(domin) + b"\r\n\r\n")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((INFRASTRUCTURE_IP, 80))
            s.sendall(b"GET " + str.encode(path) + " HTTP/1.1\r\nHost: " + str.encode(domin) + b"\r\n\r\n")
            s.close()
            time.sleep(0.1)
        except:
            pass
