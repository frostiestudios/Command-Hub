from bottle import redirect, template, static_file, route, run
import pyautogui
import os
import socket
import subprocess
import time
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)
@route("/")
def index():
    return template('client/pages/index')

@route('/restartlc')
def restartlc():
    file_path = r"C:\LoungeControl\LoungeControl-ACLauncher\LC AC Launcher.exe"
    subprocess.call(['taskkill','/F','/IM','LC AC Launcher.exe'])
    time.sleep(5)
    subprocess.Popen(file_path)
    return redirect('/')
run(host=IPAddr,port=5153,debug=True,reloader=True)