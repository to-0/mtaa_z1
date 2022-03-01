import sipfullyproxy
from sipfullyproxy import *
import socketserver
from call_logger import CallLogger
def main():
    sipfullyproxy.call_log = open('call_log.txt', 'a')
    sipfullyproxy.my_log = CallLogger(sipfullyproxy.call_log)
    print("IP address:", sipfullyproxy.ipaddress)
    server = socketserver.UDPServer((sipfullyproxy.ipaddress, 5060), UDPHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down")
        sipfullyproxy.call_log.close()

main()
