import os
path = '1'
while path != '0\\':
    os.system("cls")
    path = input("Enter the path to the folder [0 to exit]: ") + '\\'
    if path == '0\\':
        exit()
    zf = input("Enter the max number a file will get: ")
    i = int(input("Enter the starting number: "))
    os.chdir(path)
    files = os.listdir(path)
    for file in files:
        filex = file.replace(file[1], '')
        filex = filex.replace(filex[1], str(i).zfill(len(zf)))
        if filex[int(len(zf))+1] == ' ':
            filex = filex.replace(filex[int(len(zf))+1], '] ')
        os.rename(path + file, filex)
        i += 1
    print("""
+===============+
ǁ    Renamed!   ǁ 
+===============+
""")