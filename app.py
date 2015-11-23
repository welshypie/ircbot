
import irc
import network

# Receive data from socket, decode it, print to console
def receive(sock):
	msg = sock.recv(4096)		# Receive data from socket
	msg = network.decode(msg)	# Turn into a string so we can parse it
	print(msg.strip("\r\n"))	# Print to console
	return msg

# Print data to transmit to console, encode it, send to socket
def transmit(sock, msg):
	print("... " + msg.strip("\r\n"))	# Print to console
	msg = network.encode(msg)			# Encode our message
	sock.send(msg)						# Send our message

# IRC handshake used to negotiate with server and join channel
def irc_handshake(sock, nick, chan):
	# Stage 0: define what we're looking for in the transactions
	ident_trigger = "Checking Ident"
	join_trigger = "MODE"
	# Stage 1: send our ident once the server requests it
	while True:
		msg = receive(sock)
		if ident_trigger in msg:
			user_cmd = irc.user()		# Formulate USER command
			transmit(sock, user_cmd)	# Send USER command
			nick_cmd = irc.nick(nick)	# Formulate NICK command
			transmit(sock, nick_cmd)	# Send NICK command
			break
	# Stage 2: join channel once the server sets our mode
	while True:
		msg = receive(sock)
		# Check if the server has set a mode for us
		if join_trigger in msg:
			join_cmd = irc.join(chan)	# Formulate JOIN command
			transmit(sock, join_cmd)	# Send JOIN command
			break

def quit():
	pass