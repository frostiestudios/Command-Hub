import socket
import pyautogui
import os
HOST = ''  # Symbolic name meaning all available interfaces
PORT = 12345  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Waiting for a connection...')

while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024).decode()
    print(data)
    print(addr)
    if data == "SLE":
        print("Sleep Command")
        os.system("shutdown /r /t 1")



    conn.close()
    print('Connection closed.')

