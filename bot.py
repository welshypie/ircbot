
import app
import network
import socket
import sys
import time

server = sys.argv[1]	# e.g. irc.derpnet.net
channel = "#" + sys.argv[2]	# e.g. derpnet
nickname = sys.argv[3]	# e.g. derpbot

auth_users = []
trigger_dict = {}

# Create socket which will connect to the server
connection = network.create_sock(server)

# Initiate the IRC handshake sequence
# At the end of this, we will be in the specified channel
app.irc_handshake(connection, nickname, channel)
# Make this socket non-blocking with a 1.0s timeout
connection.settimeout(1.0)

while True:
	try:
		msg = app.receive(connection)
	except KeyboardInterrupt:
		connection.shutdown(socket.SHUT_RDWR)
		connection.close()
		exit("ctrl+C Interrupt detected")
	except socket.timeout:
		print("kek")