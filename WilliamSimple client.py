"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time, threading
import socket
from pythonosc import osc_message_builder
from pythonosc import udp_client

class update(threading.Thread):
    def __init__(self):
        print ("start!")
        threading.Thread.__init__(self)
        super(update, self).__init__()

    def run(self):
        # global OSCControl, server_host, playerControl
        # change = True
        # while True:
        #     try:
        #         if playerControl.p.poll() == None and change == False:
        #             print ("alive!")
        #             change = True
        #             msg = OSC.OSCMessage()
        #             msg.setAddress("/" + socket.gethostbyname(socket.gethostname()) + "/playerOpen")
        #             OSCControl.c.send(msg)
        #             print ("send!")
        #         elif playerControl.p.poll() != None and change == True:
        #             print ("close!")
        #             change = False
        #             msg = OSC.OSCMessage()
        #             msg.setAddress("/" + socket.gethostbyname(socket.gethostname()) + "/playerClose")
        #             OSCControl.c.send(msg)
        #             print ("send!")
        #     except:
        #         print ("error")
        while True:
            # client.send_message("/filter", random.random())
            client.send_message("/volume", random.random())
            time.sleep(1)



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default=socket.gethostbyname(socket.gethostname()),
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=6500,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  # print(socket.gethostbyname(socket.gethostname()))
  # client = udp_client.SimpleUDPClient(args.ip, args.port)
  client = udp_client.SimpleUDPClient(args.ip, args.port)
  # client.send_message("/volume",0)
  for x in range(10):
    client.send_message("/filter", random.random())
    time.sleep(1)
  # thread = update()
  # thread.start()