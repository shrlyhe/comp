import socket
import sys
import time

class PingClient():

	def __init__(self, ping_host, ping_port, ping_message):
		self.ping_host = ping_host
		self.ping_port = ping_port
		self.ping_message = ping_message
		self.start()

	def start(self):
		# open connection
		try:
			
			# send default msg to server
			send_time = time.time()
			ping_number = 0

			while ping_number < 10:
				ping_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				ping_sock.bind((self.ping_host, self.ping_port))

				ping_sock.sendto(self.ping_message, (self.ping_host, self.ping_port))

				# receive msg back
				received_msg = self.read_data(ping_sock)
				recv_time = time.time()
				# print("Received Time: " + str(recv_time))
				rtt = recv_time - send_time
				# print stuff out
				server_ip_address = "127.0.0.1"
				current_date = time.ctime()

				print("Reply from " + server_ip_address + ": PING " + str(ping_number) + " " + current_date +"\n" + "RTT : " + str(rtt))
				ping_number += 1
		except OSError as e:
			print("Unable to connect to socket: ", e)
			if ping_sock:
				ping_sock.close()
			sys.exit(1)

	def read_data(self, ping_sock):
		server_msg = b''
		while True:
			# receive msg
			more = ping_sock.recv(4096)
			if more == b'':
				ping_sock.close()
				sys.exit(1)
			server_msg += more

			break

		ping_sock.close()

		return server_msg

def main():
	print (sys.argv, len(sys.argv))
	ping_host = 'localhost'
	ping_port = 50007
	ping_message = 'TEST MESSAGE'
	ping_message = ping_message.encode('utf-8')

	if len(sys.argv) > 1:
		ping_host = sys.argv[1]
		ping_port = int(sys.argv[2])

	udp_client = PingClient(ping_host, ping_port, ping_message)

if __name__ == '__main__':
	main()

