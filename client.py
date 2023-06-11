import socket
import pyautogui
import os
import subprocess
import time
import webbrowser
from appJar import gui
HOST = ''  # Symbolic name meaning all available interfaces
PORT = 12345  # Arbitrary non-privileged port

hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Waiting for a connectpipion...')


#Create Simple GUI
app = gui("Client",useTtk=True,geom="200x100")
app.addLabel("HOST",f"HOST:{hostname}")
app.addLabel("IP",f"IP:{IPAddr}")
app.go()

while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024).decode()
    print(data)
    print(addr)
    if data == "S":
        print("Sleep Command")
        os.system("shutdown /s /t 1")
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
    if data == "CM":
        pyautogui.press("win")
    if data == "C":
        file_path = r"C:\LoungeControl\LoungeControl-ACLauncher\LC AC Launcher.exe"
        subprocess.call(['taskkill','/F','/IM','LC AC Launcher.exe'])
        time.sleep(5)
        subprocess.Popen(file_path)
    




    conn.close()
    print('Connection closed.')

