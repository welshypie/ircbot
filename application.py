
import irc
import network

# Receive data from socket, decode it, print to console
def receive(sock):
	# Receive data from socket
	msg = sock.recv(4096)
	# Turn into a string so we can parse it
	msg = network.decode(msg)
	# Print to console
	print(msg.strip("\r\n"))
	return msg

# Print data to transmit to console, encode it, send to socket
def transmit(sock, rsp):
	print("... " + rsp.strip("\r\n"))
	# Encode our response
	rsp = network.encode(rsp)
	sock.send(rsp)

# IRC handshake used to negotiate with server and join channel
def irc_handshake(sock, nick, chan):
	# Stage 1: send our ident once the server requests it
	while True:
		msg = receive(sock)
		if "Checking Ident" in msg:
			# Send USER command
			user_cmd = irc.user()
			transmit(sock, user_cmd)
			# Send NICK command
			nick_cmd = irc.nick(nick)
			transmit(sock, nick_cmd)
			break
	# Stage 2: join channel once the server sets our mode
	while True:
		msg = receive(sock)
		# Check if the server has set a mode for us
		if "MODE" in msg:
			join_cmd = irc.join(chan)
			transmit(sock, join_cmd)
			break