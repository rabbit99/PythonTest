# This is comments
import win32com.client
import time
import subprocess
import pyautogui


class playerControl(object):
    def __init__(self, path):
        self.path = path
        # self.subPath = ""
        print("playerControl init path = " + self.path)
        # try:
        # self.p = subprocess.Popen([self.path], shell=True)
        #   self.sp = subprocess.Popen([self.subPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        # # show server condition
        #
        # except:
        #   print("something init open error")
        #   pass

    def openPlayer(self):
        # self.p.kill()
        # TODO
        #
        self.p = subprocess.Popen([self.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        print("popen")
        self.p.wait()
        time.sleep(10)

        print("結束等待")

    def closePlayer(self):
        self.p.kill()

    def setPath(self, path):
        self.subPath = path
        print(self.path)

    def openSubProgram(self):
        self.sp.kill()
        self.sp = subprocess.Popen([self.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    def reOpenPlayer(self):
        # pyautogui.press('enter');
        self.openPlayer()
        print("按熱鍵")
        # pyautogui.hotkey('altleft', 'ctrlleft', 'f')
        pyautogui.hotkey('ctrlleft', 'n')
        # pyautogui.press('enter');


def check_exsit(process_name):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    if len(processCodeCov) > 0:
        print('%s is exists' % process_name)
        return 0
    else:
        print('%s is not exists' % process_name)
        return 1


if __name__ == "__main__":
    # TODO
    # path = AE.exe
    path = 'C:\\Users\\WILL\\AppData\\Local\\SourceTree\\SourceTree.exe'
    playerControl = playerControl(path)
    while (True):
        if check_exsit("SourceTree.exe") == 1:
            print("重啟該程式")
            playerControl.reOpenPlayer()
        time.sleep(2)
