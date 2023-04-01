from appJar import gui
import webbrowser
import json
import socket
import threading

PLY = "\u25B6"
PAU = "\u23F8"
PRE = "\u23F4"
NEX = "\u23F3"


with open('clients.json','r') as f:
    data = json.load(f)
#Load data from JSON
pcname = [pc['PCName'] for pc in data]
ips = [pc['IP'] for pc in data]
print ("PCNames:",pcname)
print ("IPs:",ips)

def send_content(btn):
    ip_address = app.getOptionBox("PCs")
    message = app.getOptionBox("Commands")
    threading.Thread(target=lambda: send(ip_address, message)).start()
    print(message)
def send(ip_address, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, 12345))
    s.sendall(message.encode())
    s.close()


app = gui("Command Hub", useTtk=True)
app.startLabelFrame("Add A New Client")

app.addButtons(["Enter"], send_content)
app.addOptionBox("PCs",ips)
app.addOptionBox("Commands",["SLE"])
app.stopLabelFrame()


app.go()
