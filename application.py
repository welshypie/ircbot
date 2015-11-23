
import irc
import network

def irc_handshake(sock, nick, chan):
	while True:
		# Receive data from socket
		msg = sock.recv(4096)
		# Turn into a string so we can parse it
		msg = network.decode(msg)
		print_rcv(data)
		# Check if the server has requested our ident
		if "Checking Ident" in msg:
			# Send USER command
			rsp = irc.user()
			print_snd(rsp)
			rsp = network.encode(rsp)
			sock.send(rsp)
			# Send NICK command
			rsp = irc.nick(nick)
			print_snd(rsp)
			rsp = network.encode(rsp)
			sock.send(rsp)
			break
	while True:
		msg = sock.recv(4096)
		msg = network.decode(msg)
		# Check if the server has set a mode for us
		if "MODE" in msg:
			rsp = irc.join(chan)
			print("... " + rsp.strip("\r\n"))
			rsp = network.encode(rsp)
			sock.send(rsp)
			break

def print_rcv(data):
	data = data.strip("\r\n")
	print(data)

def print_snd(data):
	data = "... " + data.strip("\r\n")
	print(data)