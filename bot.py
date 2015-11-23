
import app
import sys
import network

server = sys.argv[1]	# e.g. irc.derpnet.net
channel = "#" + sys.argv[2]	# e.g. derpnet
nickname = sys.argv[3]	# e.g. derpbot

auth_users = []
# response_dict = {
	# "!time":
# }

# Create socket which will connect to the server
connection = network.create_sock(server)

# Initiate the IRC handshake sequence
# At the end of this, we will be in the specified channel
app.irc_handshake(connection, nickname, channel)

while True:
	msg = app.receive(connection)