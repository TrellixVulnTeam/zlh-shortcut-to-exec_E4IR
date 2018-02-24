import subprocess
import os

batch_dir = 'C:/Users/ZLHys/ROMs/NES/bats/'
pyinstall = 'C:/Users/ZLHys/PycharmProjects/MakeBats/venv/Scripts/pyinstaller.exe'
for filename in os.listdir(batch_dir):
    print('Creating EXE for: ' + filename)
    subprocess.Popen([pyinstall,
                      batch_dir + filename,
                      "--onefile",
                      "--nowindow",
                      "--noconsole"]).wait()
