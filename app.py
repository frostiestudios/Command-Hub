from bottle import static_file, route, run, static_file, template, redirect
import socket
import webbrowser
import sqlite3
@route("/")
def index():
    return static_file("index.html",root='pages/')

@route('/leaderboard')
def leaderboard():
    return static_file("leaderboard.html",root='pages/')

@route('/leaderboard/new')
def leaderboardnew():
    webbrowser.open("https://192.168.1.12:6001/remoteview/?id=1")
    redirect("/leaderboard")

#Start-Up Settings
@route('/setup')
def start():
    return static_file("startup.html", root='pages/')

@route('/setup/computers')
def computers():
  print("computers")
  conn = sqlite3.connect('rr.db')
  c = conn.cursor()
  c.execute("SELECT id, ip, name FROM computers")
  result = c.fetchall()
  c.close()
  output = template('pages/sigma',rows=result)
  return output

@route('/remcom')
def remcom():
    print('remote commander....')
    conn = sqlite3.connect('rr.db')
    c = conn.cursor()
    c.execute("SELECT id, ip, name FROM computers")
    result = c.fetchall()
    c.close()
    output = template('pages/remcom',rows=result)
    return output


hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)
run(host=IPAddr,port=5152,reloader=True,debug=True)