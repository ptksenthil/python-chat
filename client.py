import socket
import threading
host = socket.gethostname() 
port = 8000
s = socket.socket() 
s.connect((host, port))
print(' CONNECTED TO %s ' % (host))
while True:

    d=input('reply to server > ')
    s.sendall(d.encode('ascii'))
    if not d:
        break
    r=s.recv(1024)
    print('msg from server> ',r.decode('ascii'))
    if not r:
        break

s.close()
    
    
       
