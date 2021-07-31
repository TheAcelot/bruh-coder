import base64
def encode(data):
	buffer = b''
	start = data.encode("utf-8") #encode data in utf-8
	for x in range(len(start)):
		final = base64.b64encode(start)#encode in 64
		buffer += final
	fin = base64.b32encode(buffer) #encode all in 32
	print(fin) #result

def decode(data):
	start = base64.b32decode(data) #decode in 32
	for x in range(1):		#int(len(data))
		final = base64.b64decode(start)#decode in 64
	utf = final.decode("utf-8")
	print(utf) #result
#example usage:
	#encode("text")
	#decode(b'bytes')