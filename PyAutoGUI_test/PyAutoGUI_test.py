import pyautogui
import time

# print(pyautogui.locateOnScreen('github.png'))
#
# pyautogui.center(pyautogui.locateOnScreen('github.png'))  #  取得該圖像的中間值(1519，146)
# print(pyautogui.center(pyautogui.locateOnScreen('github.png')))
# pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen('github.png')))  #  點擊
# time.sleep(5)
try:
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('wmr.png')))       #运行别的代码
except:
    print("err")       #如果在try部份引发了'name'异常
else:
    print("right")  #如果没有异常发生
time.sleep(1)
# time.sleep(1)
pyautogui.keyDown('altleft', 'space')
time.sleep(1)
pyautogui.press('x');

try:
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('wakeUp.png')))       #运行别的代码
except:
    print("運行中")       #如果在try部份引发了'name'异常
else:
    print("已喚醒")  #如果没有异常发生

time.sleep(0.5)

try:
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('wmr2.png')))       #运行别的代码
except:
    print("沒有偵測到側邊")       #如果在try部份引发了'name'异常
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('wmr2_1.png')))
    except:
        print("再次沒有偵測到側邊")
else:
    print("有偵測到側邊")  #如果没有异常发生

time.sleep(0.5)

try:
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('wmr3.png')))      #运行别的代码
except:
    print("沒有偵測到房間邊界按鈕")       #如果在try部份引发了'name'异常
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('wmr3_1.png')))
else:
    print("有偵測到房間邊界按")  #如果没有异常发生

time.sleep(0.5)
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('wmr4.png')))
time.sleep(0.5)
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('wmr5.png')))
time.sleep(0.5)
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('wmr6.png')))
time.sleep(0.5)
pyautogui.hotkey('altleft', 'space','n')
pyautogui.press('n');