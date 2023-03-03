import socket
import pyautogui
import webbrowser
import os
import subprocess
from appJar import gui

print("Client Now Active")
print("Built By Frostie Studios")
print("View on GitHub: https://github.com/frostiestudios/RRSM")
tricommand = input("Insert 3 Letter TriCommand")
if tricommand == 'NUT':
        print("Running a command")
        webbrowser.open("https://www.youtube.com/watch?v=9bSGlMd1Y7Q")
        print("It's the nutshack")
        pyautogui.sleep(2)
        pyautogui.press('space')
if tricommand == 'TR1':
    subprocess.run(["python", "homepage/files/acjoin.py"])
def receive_message():
    # Create a socket and listen for incoming connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 12345))
    s.listen(1)
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    data = conn.recv(1024).decode()
    print(f"Received: {data}")
    if data=="CO1":
        open("homepage/files/acjoin.py") 
    conn.close()
    receive_message()
    
# Create a loop to continuously listen for incoming connections
while True:
    receive_message()
