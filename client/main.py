import socketserver
import time
import threading
import socket
import sys

class MyUDPHandler(socketserver.BaseRequestHandler):
  def handle(self):
    data = self.request[0].strip()
    sock = self.request[1]
    print("{} wrote:".format(self.client_address[0]))
    print(data)
    sock.sendto(data.upper(), self.client_address)

def spam():
  cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  cs.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  while True:
    cs.sendto(sys.argv[1].encode(), ('255.255.255.255', 41234))
    time.sleep(0.5)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Missing Beacon ID parameter!")
    sys.exit(1)
  threading.Thread(target=spam).start()
  HOST, PORT = "127.0.0.1", 41235
  with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
    server.serve_forever()
