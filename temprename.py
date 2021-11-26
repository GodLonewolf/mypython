import os
path = input("Path") + '\\'
zf = 2
os.chdir(path)
i = 1
files = os.listdir(path)
for file in files:
    os.rename(path + file, file+str(i)+'.jpg')
    i += 1