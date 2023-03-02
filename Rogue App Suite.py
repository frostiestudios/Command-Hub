from appJar import gui
import webbrowser

def openApp():
    print("opening app")
def link():
    webbrowser.open("https://github.com/frostiestudios/Rogue-App-Suite")

app = gui("Rogue App Suite", useTtk=True)
app.startTabbedFrame("Tabs")

app.startTab("Home")
app.addLabel("Rogue App Suite")
app.addLabel("a1", "Command Hub")
app.addButtons(["Open"], openApp)
app.stopTab()

app.startTab("About")
app.addMessage("Designed by Frostie Studios 2022")
app.addButton("View On GitHub",link)
app.stopTab()
app.stopTabbedFrame()
app.go()
