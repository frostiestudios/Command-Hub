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
    if data == "S":
        print("Sleep Command")
        os.system("shutdown /r /t 1")
    #ASSETTO COMMANDS
    if data == "B":
        pyautogui.keyDown("ctrlleft")
        pyautogui.keyDown("b")
        pyautogui.keyUp("ctrlleft")
        pyautogui.keyUp("b")
        print("Driver Sent to Pits")
    if data == "G":
        pyautogui.keyDown("ctrlleft")
        pyautogui.keyDown("g")
        pyautogui.keyUp("ctrlleft")
        pyautogui.keyUp("g")


    conn.close()
    print('Connection closed.')

