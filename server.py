import socket

#make socket
s = socket.socket()
#definite port 3000
port = 3000
s.bind(('', port))
print ('\nSocket binded to',port)

#listening mode
s.listen(5)
print ('\nSocket is listening ...')
#accept the request connection from client
c, addr = s.accept()
print ('\nGot connection from ', addr)

while True:
	#receive data send by client
	data = c.recv(1024)
	#decode, because client send it in bytes conversion
	data = data.decode('utf-8')
	print (data)
	#split the data
	data = data.split(' ')
	for i in range(3):
		print ('data',i,':',data[i])
	#make the operand become an integer not bytes/string
	data[0] = int(data[0])
	data[2] = int(data[2])

	#condition to calculate
	if data[1]=='*':
		res = data[0]*data[2]
	elif data[1]=='/':
		res = int(data[0]/data[2]) #in order to the result is not float data type
	elif data[1]=='+':
		res = data[0]+data[2]
	elif data[1]=='-':
		res = data[0]-data[2]
	else: #if client input the operator exclude 4 operator provided by server
		print ('The operand is not defined in this socket.')

	print ('result is',res,'\n')
	#result send to the client in encode bytes again
	res = bytes(str(res), 'utf-8')
	c.send(res)

#server close
s.close()