import socket

c=socket.socket()
print("socket created")
c.connect(('localhost',9999))
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


		