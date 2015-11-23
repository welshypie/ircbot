'''
Taking parameters as inputs, formulate the message to be sent to the server
for a particular IRC command.

'''

# Send ping to server
# def ping(svr1, svr2=""):
	# if svr2 == "":
		# pass
	# else:
		# svr2 = " " + svr2
	# cmd = "PING " + svr1 + svr2 + "\n"
	# return cmd

# Reply to server ping
def pong(svr):
	cmd = "PONG " + svr + "\r\n"
	return cmd

# Send message to channel or user
def privmsg(tgt, msg): 
	cmd = "PRIVMSG " + tgt + " :" + msg + "\r\n"
	return cmd

# Join a single specified channel
def join(chan):
	cmd = "JOIN " + chan + "\r\n"
	return cmd

# Leave a single specified channel
def part(chan, msg=""):
	cmd = "PART " + chan + " :" + msg + "\r\n"
	return cmd

# Quit server
def quit(msg=""):
	cmd = "QUIT :" + msg + "\r\n"
	return cmd

# Set username, mode 8 sets invisible and the rest is garbage
def user(user="guest", mode="8", realname="lol idk"):
	cmd = "USER " + user + " " + mode + " * :" + realname + "\r\n"
	return cmd

# Set nick
def nick(name):
	cmd = "NICK " + name + "\r\n"
	return cmd