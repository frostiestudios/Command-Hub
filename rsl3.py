from http.server import HTTPServer, SimpleHTTPRequestHandler
from appJar import gui
import socket
import os
import subprocess
import threading
import webbrowser

PLY = "\u25B6"
PAU = "\u23F8"
PRE = "\u23F4"
NEX = "\u23F3"


def mk(btn):
    if btn == "Start":
        print("Server Starting Up")
        subprocess.call(['mkdocs', 'serve'], cwd='localserver')
        print("Server Now Live")
    if btn == "Build":
        print("Building")
        subprocess.call(['mkdocs', 'build'], cwd='localserver')


def openmk(btn):
    if btn == "Open Localhost":
        print("Opening Site")


def server(btn):
    if btn == PLY:
        host_name = socket.gethostbyname(socket.gethostname())
        port_number = 5151
        # Create an HTTP server
        httpd = HTTPServer((host_name, port_number), SimpleHTTPRequestHandler)
        # Start the server in a separate thread
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.start()
        app.setLabel("SL", f"Server: http://{host_name}:{port_number}")
        app.setLabel("SS", "Online")
        print("Server started at http://{}:{}/localserver/site/".format(*httpd.socket.getsockname()))
    if btn == PAU:
        host_name = socket.gethostbyname(socket.gethostname())
        port_number = 5151
        httpd = HTTPServer((host_name, port_number), SimpleHTTPRequestHandler)
        server_thread = threading.Thread(target=httpd.serve_forever)
        httpd.shutdown()
        httpd.server_close()
        server_thread.join()
        app.setLabel("SL", "Server: Offline")
        app.setLabel("SS", "Server: Offline")
        print("Server stopped.")
        app.infoBox("Server stopped", "Server has been stopped successfully")


def serversettings():
    print("Settings")


app = gui("RSL 3", useTtk=True)
app.startLabelFrame("Server Controls")
app.addButtons([PLY, PAU], server)
app.addButtons(["Build"], mk)
app.stopLabelFrame()

app.startLabelFrame("Server Status")
app.addLabel("SL")
app.addLabel("SS")
app.stopLabelFrame()

app.startLabelFrame("Open")
app.addButtons(["Open Localhost", "Open Remote"], openmk)
app.stopLabelFrame()

app.startLabelFrame("Settings")
app.addLabelOptionBox("Style", ["Dark", "Light"])
app.addLabelEntry("Name")
app.stopLabelFrame()
app.go()
