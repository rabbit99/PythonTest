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
    # try:
    #   self.p = subprocess.Popen([self.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    # show server condition

    # except:
    #   pass

  def openPlayer(self, addr, tags):
    # self.p.kill()
    self.p = subprocess.Popen([self.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)



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
    self.dispatcher.map("/clientSetup", playerControl.openPlayer)
    self.dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)

    self.server = osc_server.ThreadingOSCUDPServer(
      (self.args.ip, self.args.port), self.dispatcher)
    print("Serving on {}".format(self.server.server_address))
    self.server.serve_forever()

if __name__ == "__main__":

  # parser = argparse.ArgumentParser()
  # parser.add_argument("--ip",
  #     default=socket.gethostbyname(socket.gethostname()), help="The ip to listen on")
  # parser.add_argument("--port",
  #     type=int, default=6500, help="The port to listen on")
  # args = parser.parse_args()
  #
  # path = 'C:\\Funique\\ClientEXE\\Funique_Client.exe'
  # playerControl = playerControl(path)
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

  input()


