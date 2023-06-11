import os
import webbrowser
from appJar import gui
def command(btn):
    if btn=="Leaderboard":
        webbrowser.open("https://192.168.1.12:6001/remoteview/?id=1")
        print("WebBrowser 1 Now Openeded")
        print("View Me At https://192.168.1.12:6001/remoteview/?id=1")
app = gui("50x100")
app.addLabel("Press a Command","please press a comand")
app.addButton("Leaderboard",command)
app.go()