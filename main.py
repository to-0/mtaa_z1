from sipfullyproxy import *
import socketserver

def main():
    print("IP address:", ipaddress)
    server = socketserver.UDPServer((ipaddress, 5060), UDPHandler)
    server.serve_forever()


main()