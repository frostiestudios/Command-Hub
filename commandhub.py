from appJar import gui
import webbrowser
import json

PLY= "\u25B6"
PAU= "\u23F8"
PRE= "\u23F4"
NEX= "\u23F3"

with open('commands.json') as f:
    data = json.load(f)
print("commands.json loaded")
print("Welcome to Custom Command Hub")


def newcommand(btn):
    name = app.getEntry("Script Name")
    lang = app.getEntry("Language")
    new_command = {"name:": name, "language:": lang}
    data["commands"].append(new_command)
    with open('commands.json', 'w') as file:
        json.dump(data, file, indent=2)
    app.setEntry("Script Name", "")
    app.setEntry("Language", "")


app = gui("Command Hub", useTtk=True)
app.startTabbedFrame("Tabs")
app.startTab("Home")
app.addLabel("l1","Welcome",1,1)
app.addImage("i1",'icons/radio.png',1,2)


app.stopTab()

app.startTab("New Command")
app.startLabelFrame("Add A New Client")
app.addLabelEntry("Script Name")
app.addLabelEntry("Language")
app.addButtons(["Enter"], newcommand)
app.stopLabelFrame()
app.stopTab()

app.go()
