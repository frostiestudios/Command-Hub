# import modules
from tkinter import *
from tkinter import ttk
import webbrowser
import subprocess
import time
import os
 
 
# user define function
def shutdown():
    return os.system("shutdown /s /t 1")
 
def restart():
    return os.system("shutdown /r /t 1")
 
def logout():
    return os.system("shutdown -l")

def restartlc():
    file_path = r"C:\LoungeControl\LoungeControl-ACLauncher\LC AC Launcher.exe"
    subprocess.call(['taskkill','/F','/IM','LC AC Launcher.exe'])
    time.sleep(5)
    subprocess.Popen(file_path) 


root = Tk()
root.title("Command Hub")
root.geometry("500x200")

ttk.Label(root,text="PowerCommands").grid()
ttk.Button(root,text="Shutdown").grid()
ttk.Button(root,text="Restart").grid()
root.mainloop()