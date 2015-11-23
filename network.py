
import socket

# Take a hostname or IP and port (default 6667), return a socket object
def create_sock(svr, port=6667):
	print("... Creating socket")
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("... Attempting to connect to " + svr + ":" + str(port))
	sock.connect((svr, port))
	print("... Connection successful!")
	return sock

# Encode string to UTF-8 bytes
def encode(input_str):
	encoded = bytes(input_str, 'utf-8')
	return encoded

# Decode data bytes to UTF-8 string
def decode(raw_bytes):
	decoded = raw_bytes.decode('utf-8')
	return decoded

'''
Non-blocking socket timeout info
http://stackoverflow.com/questions/16745409/what-does-pythons-socket-recv-return-for-non-blocking-sockets-if-no-data-is-r
'''