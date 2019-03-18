# This is comments
import win32com.client
import time
import subprocess
import pyautogui


class playerControl(object):
    def __init__(self, p_path,p_process_name,p_waitSec):
        self.pl_path = p_path
        self.pl_process_name = p_process_name
        self.pl_waitSec = p_waitSec
        # self.subPath = ""
        print("playerControl init path = " + self.pl_path)
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
        print("popen = "+self.pl_path)
        # self.p = subprocess.Popen([self.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        self.p = subprocess.Popen([self.pl_path], shell=True)
        self.p.wait()
        time.sleep(float(self.pl_waitSec))

        print("結束等待"+self.pl_waitSec)

    def reOpenPlayer(self):
        # pyautogui.press('enter');
        self.openPlayer()
        print("按熱鍵")
        pyautogui.hotkey('altleft', 'ctrlleft', '0')
        # pyautogui.hotkey('ctrlleft', 'n')
        time.sleep(float(self.pl_waitSec))
        pyautogui.press('enter');

    def check_exsit(self,xx_process_name):
        WMI = win32com.client.GetObject('winmgmts:')
        # test = r'SourceTree.exe'
        processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % xx_process_name)
        if len(processCodeCov) > 0:
            print('%s is exists' % xx_process_name)
            return 0
        else:
            print('%s is not exists' % xx_process_name)
            return 1




def check_path():
    try:
        f = open('path.txt', 'r')  # 运行别的代码
    except:
        print("無此txt 新建立一個")  # 如果在try部份引发了'name'异常
        f = open('path.txt', 'w')
        lines = ['10\n','C:\\Users\\WILL\\AppData\\Local\\SourceTree\\SourceTree.exe\n', 'SourceTree.exe']
        f.writelines(lines)
    else:
        print("有此檔案")  # 如果没有异常发生

    f = open('path.txt', 'r')
    path = []
    for line in f:
        path.append(line)
        print(line)
    print(path)
    return path

if __name__ == "__main__":
    # TODO
    # path = AE.exe
    in_path = check_path()
    playerControl = playerControl(in_path[1],in_path[2],in_path[0])

    while (True):
        if playerControl.check_exsit(in_path[2]) == 1:
            print("重啟該程式 = "+in_path[2])
            playerControl.reOpenPlayer()
        time.sleep(2)
