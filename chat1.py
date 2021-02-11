from socket import *

s=socket()
print("socket created")
s.bind(('localhost',9999))
s.listen(3)
print("wait for connection")
while True:
    c,addr=s.accept()
    print("connected with",addr)
    c.send(bytes('welcome to newchart','utf-8'))
    while True:
    	
    	#r=input('enter the "r" to recive message to send message enter "c"')
    	#if r=='r':
    	print(c.recv(1024).decode())
    	#elif r=='c':
    	chat=input("enter the chat: ")
    	c.send(bytes(chat,'utf-8'))

    	
    	if chat=='end':
    		break
    c.close()
    break
    
  