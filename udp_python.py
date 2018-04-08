import socket
import sys


class PingServer():

	def __init__(self, ping_server_host, ping_server_port):
		self.ping_server_host = ping_server_host
		self.ping_server_port = ping_server_port
		self.start()

	def start(self):
		# Initialize server socket on which to listen for connections
		try:
			ping_server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			ping_server_sock.bind((self.ping_server_host, self.ping_server_port))

		except OSError as e:
			print ("Unable to open server socket")
			if ping_server_sock:
				ping_server_sock.close()
			sys.exit(1)

		client_msg = self.read_data(ping_server_sock)
		
		print("THIS IS THE MSG: " + client_msg.decode('utf-8'))
		self.send_data(ping_server_sock, client_msg)

		# send msg back to client
		# ping_server_sock.sendall(client_msg)
		

	def read_data(self, ping_server_sock):
		client_msg = b''
		while True:
			# receive msg
			msg = ping_server_sock.recv(4096)
			if not msg:
				self.cleanup(ping_server_sock)
				break
			break
		client_msg += msg

		return client_msg

	def send_data(self, ping_server_sock, client_msg):
		ping_server_sock.sendto(client_msg, (self.ping_server_host, self.ping_server_port))
		print("SENT DATA" + client_msg.decode('utf-8'))




def main():

	print (sys.argv, len(sys.argv))
	ping_server_host = 'localhost'
	ping_server_port = 50007

	if len(sys.argv) > 1:
		ping_server_host = sys.argv[1]
		ping_server_port = int(sys.argv[2])

	udp_python = PingServer(ping_server_host, ping_server_port)

if __name__ == '__main__':
	main()




