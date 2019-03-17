


try:
    f = open('path.txt','r')     #运行别的代码
except:
    print("無此txt 新建立一個")       #如果在try部份引发了'name'异常
    f = open('path.txt', 'w')
    value = "預設"
    f.write(value)
else:
    print("有此檔案")  #如果没有异常发生



f = open('path.txt','r')
print(f.read())