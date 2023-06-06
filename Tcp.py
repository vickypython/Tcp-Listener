import socket
TCP_IP = "192.168.70.1"
TCP_PORT= 3000
BUFFER_SIZE = 100
s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(1)
conn,addr = s.accept()
print('connection address:',addr)
while True:
    data =conn.recv(BUFFER_SIZE)
    if not data:
        break
    print("Received data:",data)
    conn.send(data) #echo
    conn.close()
    