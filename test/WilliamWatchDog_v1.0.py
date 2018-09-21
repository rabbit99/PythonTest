"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math
import socket
import subprocess
from pythonosc import dispatcher
from pythonosc import osc_server
from subprocess import STDOUT, check_output

class playerControl(object):
  def __init__(self, path):
    self.path = path
    self.subPath = ""
    print("playerControl init path = "+self.path)
    try:
      self.p = subprocess.Popen([self.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      self.sp = subprocess.Popen([self.subPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    # show server condition

    except:
      print("something init open error")
      pass

  def openPlayer(self):
    self.p.kill()
    self.p = subprocess.Popen([self.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

  def closePlayer(self):
    self.p.kill()

  def setPath(self,path):
    self.subPath = path
    print(self.path)

  def openSubProgram(self):
    self.sp.kill()
    self.sp = subprocess.Popen([self.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)



def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

def print_compute_handler(unused_addr, args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass


class Osccontrol():
  def __init__(self):
    self.server_init()

  def server_init(self):
    self.parser = argparse.ArgumentParser()
    self.parser.add_argument("--ip",
                             default=socket.gethostbyname(socket.gethostname()), help="The ip to listen on")
    self.parser.add_argument("--port",
                             type=int, default=6500, help="The port to listen on")
    self.args = self.parser.parse_args()

    # self.path = 'C:\\Funique\\ClientEXE\\Funique_Client.exe'

    self.dispatcher = dispatcher.Dispatcher()
    self.dispatcher.map("/filter", print)
    self.dispatcher.map("/clientSetup", print)
    self.dispatcher.map("/FromServer", self.ServerRecived)
    self.dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)

    self.server = osc_server.ThreadingOSCUDPServer(
      (self.args.ip, self.args.port), self.dispatcher)
    print("Serving on {}".format(self.server.server_address))
    self.server.serve_forever()

  def ServerRecived(self, addr, tags):
    print(addr)
    print(tags)
    # print (tags.split("/"))
    if tags.split("/")[0] == "123":
      print("有123 = "+tags.split("/")[2])
    elif tags.split("/")[0] == "openPlayer":
      playerControl.openPlayer()
    elif tags.split("/")[0] == "closePlayer":
      playerControl.closePlayer()
    # print (tags.split(' ', 1))

if __name__ == "__main__":

  # parser = argparse.ArgumentParser()
  # parser.add_argument("--ip",
  #     default=socket.gethostbyname(socket.gethostname()), help="The ip to listen on")
  # parser.add_argument("--port",
  #     type=int, default=6500, help="The port to listen on")
  # args = parser.parse_args()
  #
  path = 'C:\\Funique\\ClientEXE\\Funique_Client.exe'
  # path = 'C:\\Funique\\ClientEXE\\scratch.py'
  playerControl = playerControl(path)
  #
  # dispatcher = dispatcher.Dispatcher()
  # dispatcher.map("/filter", print)
  # dispatcher.map("/clientSetup", playerControl.openPlayer)
  # dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)
  #
  # server = osc_server.ThreadingOSCUDPServer(
  #     (args.ip, args.port), dispatcher)
  # print("Serving on {}".format(server.server_address))
  # server.serve_forever()

  o = Osccontrol()



