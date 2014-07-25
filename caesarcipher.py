import sys
def get(plaintext, key=3): #you can change this to any key you'd like or modify it so that it will take a key as input
	cipher = ''
	for each in plaintext:
		c = (ord(each)+key) % 126         
		if c < 32:
			c+=31
		cipher += chr(c)
	return cipher
while 1:
	l = sys.stdin.readline()
	print get(l).replace(",", '')
