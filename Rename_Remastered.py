import os
path = '1'
while path != '0\\':
    path = input("Enter the path to the folder [0 to exit]: ") + '\\'
    if path == '0\\':
        exit()
    zf = input("Enter the max number a file will get: ")
    txt = input("Enter the text to rename the files: ")
    ext = input("Enter an extension (without a '.'): ")
    sep = input("Enter a separator: ")
    i = int(input("Enter the starting number: "))
    r1 = input("1. To add text before numbering\n2. To add numbering before text\nEnter [1/2]: ")
    os.chdir(path)
    files = os.listdir(path)
    if r1 == '1':
        for file in files:
            os.rename(path + file, txt + ' {} '.format(sep) + str(i).zfill(len(zf)) + '.' + ext)
            i += 1
        print("""
+===============+
ǁ    Renamed!   ǁ 
+===============+
""")
    elif r1 == '2':
        for file in files:
            os.rename(path + file, str(i).zfill(len(zf)) + ' {} '.format(sep) + txt + '.' + ext)
            i += 1
        print("""
+===============+
ǁ    Renamed!   ǁ 
+===============+
""")