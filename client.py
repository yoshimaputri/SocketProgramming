import socket

#make a socket
c = socket.socket()
print ('\n-- WELCOME TO SOCKET CALCULATOR --\n')

#connect to server -> input IP
print ('Please input the ip server')
ipserver = input()
c.connect((ipserver,3000))

yes=1
while yes:
	#input operator and 2 operands
	operator = input('\nInput the operator    : ')
	operand1 = input('Input the 1st operand : ')
	operand2 = input('Input the 2st operand : ')

	#make input become 1 data for sending to server (bytes)
	data = bytes(str('{0} {1} {2}'.format(operand1, operator, operand2)), 'utf-8')
	c.send(data)

	#show the result from the input (receive result from server, max 1024 bytes)
	print ('\nThe result from ',operand1,operator,operand2,'=',int(c.recv(1024)))

	#condition to loop calculator or stop it
	l = input('\nDo you want to Continue (Y/N) ?')
	if l=='y' or l=='Y':
		continue
	else: #exit the program (not to be continued)
		yes=0
		print ('\nThank you to use our product.\nAuth : yoshima01')
		
#client close
c.close()