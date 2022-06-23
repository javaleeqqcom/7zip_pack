import py7zr
import time
import numpy as np

file1= r"D:\新建文件夹\test.7z"
file2= r"D:\新建文件夹\test_big.7z"


rd_times=1
rdps= list(map(str,np.random.randint(0,(1<<30)-1,rd_times)))
ret=None
bg = time.time()
for i in range(rd_times):
    with py7zr.SevenZipFile(file1,"r",password=rdps[i]) as obj:
        try:
            obj.testzip()
            ret = True
        except:
            ret = False
end = time.time()
print(ret)
print("cost:{:.3f}s".format(end-bg))

with py7zr.SevenZipFile(file2,"r",password="123456789") as obj:
    print(obj.testzip())