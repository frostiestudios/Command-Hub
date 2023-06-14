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
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname)
    return template('client/pages/index', IPAddr=IPAddr,host=hostname)

@route('/restartlc')
def restartlc():
    file_path = r"C:\LoungeControl\LoungeControl-ACLauncher\LC AC Launcher.exe"
    subprocess.call(['taskkill','/F','/IM','LC AC Launcher.exe'])
    time.sleep(5)
    subprocess.Popen(file_path)
    return redirect('/')
@route('/logout')
def logout():
    print ("Logging Out")
    os.system("shutdown -l")
run(host=IPAddr,port=5153,debug=True,reloader=True)