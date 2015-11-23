
import application
import sys

server = sys.argv[1]	# e.g. irc.derpnet.net
channel = sys.argv[2]	# e.g. derpnet
nickname = sys.argv[3]	# e.g. derpbot

auth_users = []
command_dict = {}

# Create socket which will connect to the server
connection = network.create_sock(server)

# Initiate the IRC handshake sequence
# At the end of this, we will be in the specified channel
application.irc_handshake(connection, nickname, channel)

