import subprocess
import OSC
import time, threading
import socket
from subprocess import STDOUT, check_output
import os
import sys
from ftplib import FTP

class FTPDownload(object):
	def __init__(self, fold):
		super(FTPDownload, self).__init__()
		self.result = []
		self.fold = fold
						
	def FTPWalk(self, path):
		if self.ftp.nlst(path)[0] == path:
			self.result.append(path)
		elif(self.ftp.nlst(path) != []):
			for s in self.ftp.nlst(path):
				self.FTPWalk(s)

	def FTPCoverFilesUpdate(self, addr, tags, args, source):
		print ("Enter FTPCoverFilesUpdate!")

		self.ftp = FTP('192.168.1.229')
		self.ftp.login('rick', 'bjodk')
		self.result = []
		for p in self.ftp.nlst():
			self.FTPWalk(p)
		for r in self.result:
			selfFold = self.fold + r
			if os.path.isdir(selfFold) == False:
				selfFold = os.path.dirname(selfFold)
			if os.path.exists(selfFold) == False:
				os.makedirs(selfFold)
			self.ftp.retrbinary('RETR ' + r, open(self.fold + r, 'wb').write)
		print ("End FTPCoverFilesUpdate!")

	def FTPDifferentationUpdate(self, addr, tags, args, source):
		print ("Enter FTPDifferentationUpdate!")

		self.ftp = FTP('192.168.1.229')
		self.ftp.login('rick', 'bjodk')
		self.result = []
		for p in self.ftp.nlst():
			self.FTPWalk(p)
		for r in self.result:
			print ("enter!!!")
			if os.path.exists(self.fold + r) == False:
				print ("hi")
				selfFold = self.fold + r
				if os.path.isdir(selfFold) == False:
					selfFold = os.path.dirname(selfFold)
				if os.path.exists(selfFold) == False:
					os.makedirs(selfFold)
				self.ftp.retrbinary('RETR ' + r, open(self.fold + r, 'wb').write)
		print ("End FTPDifferentationUpdate!")

def helloWorld(addr, tags, args, source):
	print ("hello world!")
	print (addr)
	print (tags)
	print (args)
	print (source)
def reboot(addr, tags, args, source):
	os.system("shutdown -t 0 -r -f")
def shutdown(addr, tags, args, source):
	os.system("shutdown -t 0 -s -f")

class playerControl(object):
	"""docstring for playerControl"""
	def __init__(self, path):
		self.path = path
		try:
			self.p = subprocess.Popen([self.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			#show server condition
			
		except:
			pass

	def openPlayer(self, addr, tags, args, source):
		os.system("taskkill /f /im vrmonitor.exe")
		self.p.kill()
		self.p = subprocess.Popen([self.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

	def closePlayer(self, addr, tags, args, source):
		self.p.kill()
		os.system("taskkill /f /im vrmonitor.exe")		
		
	def thisPopen(self):
		return self.p.poll()


class subPlayerControl(object):
	"""docstring for subPlayerControl"""

	def __init__(self, path):
		self.path = path
		try:
			self.p = subprocess.Popen([self.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
		# show server condition

		except:
			pass

	def openPlayer(self, addr, tags, args, source):
		self.p.kill()
		self.p = subprocess.Popen([self.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

	def closePlayer(self, addr, tags, args, source):
		self.p.kill()

class update(threading.Thread):
	def __init__(self):
		print ("start!")
		threading.Thread.__init__(self)
		super(update, self).__init__()
	def run(self):
		global OSCControl, server_host, playerControl
		change = True
		while True:
			try:
				if playerControl.p.poll() == None and change == False:
					print ("alive!")
					change = True
					msg = OSC.OSCMessage()
					msg.setAddress("/" + socket.gethostbyname(socket.gethostname()) + "/playerOpen")
					OSCControl.c.send(msg)
					print ("send!")
				elif playerControl.p.poll() != None and change == True:
					print ("close!")
					change = False
					msg = OSC.OSCMessage()
					msg.setAddress("/" + socket.gethostbyname(socket.gethostname()) + "/playerClose")
					OSCControl.c.send(msg)
					print ("send!")
			except:
				print ("error")
			time.sleep(1)
'''
			if OSCControl.s.running == False:
				print "ready to restart"
				time.sleep(5)
				print "restart"
				OSCControl.s = OSC.OSCServer(server_host)
				OSCControl.addAddress()
				OSCControl.st = threading.Thread( target = OSCControl.s.serve_forever )
				OSCControl.st.start()'''

            #print p.poll()
            #print "\n"

class OSCControl(object):

	def __init__(self, server_host):
		super(OSCControl, self).__init__()
		self.c = OSC.OSCClient()
		self.s = OSC.OSCServer(server_host)

		#osc address
		self.addAddress()

		#server forever
		self.st = threading.Thread( target = self.s.serve_forever )
		self.st.start()

	def addAddress(self):
		#test
		self.s.addMsgHandler("/hi",helloWorld)
		
		#from server
		self.s.addMsgHandler("/openPlayer",playerControl.openPlayer)
		self.s.addMsgHandler("/closePlayer",playerControl.closePlayer)
		self.s.addMsgHandler("/FTPDifferentationUpdate", FTPDownload.FTPDifferentationUpdate)
		self.s.addMsgHandler("/FTPCoverFilesUpdate", FTPDownload.FTPCoverFilesUpdate)
		self.s.addMsgHandler("/reboot", reboot)
		self.s.addMsgHandler("/closeServer", self.closeServer)
		self.s.addMsgHandler("/clientSetup", self.clientSetup)
		self.s.addMsgHandler("/shutdown", shutdown)

		#from player conditional
		self.s.addMsgHandler("/alive", self.playerConditional)

		#shutdown server
	def closeServer(self, addr, tags, args, source):
		self.s.close()
		print ("shutdown")

	def playerConditional(self, addr, tags, args, source):
		print ("still alive!")

	def clientSetup(self, addr, tags, args, source):
		global playerControl
		print (args[0] + " is connect!")
		client_host = args[0],7002
		self.c.connect(client_host)
		try:
			msg = OSC.OSCMessage()
			msg.setAddress("/clientSetup")
			msg.append(socket.gethostbyname(socket.gethostname()))
			self.c.send(msg)
			if playerControl.p.poll() == None:
				msg = OSC.OSCMessage()
				msg.setAddress("/" + socket.gethostbyname(socket.gethostname()) + "/playerOpen")
				self.c.send(msg)	
			elif playerControl.p.poll() != None:
				msg = OSC.OSCMessage()
				msg.setAddress("/" + socket.gethostbyname(socket.gethostname()) + "/playerClose")
				self.c.send(msg)		
		except:
			print ("error")

if __name__ == '__main__':
	print (sys.argv)
	print (socket.gethostbyname(socket.gethostname()))
	#open path & server ip, port
	path = 'C:\\Funique\\ClientEXE\\Funique_Client.exe'
	# subPath = 'C:\\Funique\\ClientEXE\\Funique_Client.exe'
	fold = os.path.dirname(os.path.dirname(path)) + '\\'
	server_host = socket.gethostbyname(socket.gethostname()),6500

	for comandLine in sys.argv:
		if "-path-" in comandLine:
			path = comandLine.replace("-path-", "")
			fold = os.path.dirname(os.path.dirname(path)) + '\\'
			print (path)
		elif "-ip-" in comandLine:
			server_host = comandLine.replace("-ip-", "")
			print (server_host)
	

	playerControl = playerControl(path)
	# subPlayerControl = subPlayerControl(subPath)
	# FTPDownload = FTPDownload(fold)
	OSCControl = OSCControl(server_host)
	
	thread = update()
	thread.start()





