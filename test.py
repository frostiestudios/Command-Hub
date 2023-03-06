from appJar import gui
import webbrowser
import json
import subprocess


def actions(btn):
    if btn == "Go":
        print("Server Has Been Created")
        sn = app.getEntry("Server Name")
        sl = app.getEntry("Server Location")
        print(f"Server Name: {sn}")
        print(f"Server Location: {sl}")
        subprocess.call(['mkdocs', 'new'], cwd=sl)


app = gui("RSL Setup", useTtk=True)
app.addLabel("Ttl", "Setup")
app.addDirectoryEntry("Server Location")
app.addLabelEntry("Server Name")
app.addButtons(["Go"], actions)
app.go()
