import os
path = 'C:\Personal Files\Anime\% The God Of Highschool\\'
os.chdir(path)
files = os.listdir(path)
i = 1
for file in files:
    os.rename(path + file, str(i).zfill(2) + ' - GOH' + '.mkv')
    i += 1