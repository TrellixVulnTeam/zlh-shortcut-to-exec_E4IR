import os

root_dir = 'C:/Users/ZLHys/ROMs/GB/roms/'
batch_dir = 'C:/Users/ZLHys/ROMs/GB/bats/'
emu = 'C:/Users/ZLHys/ROMs/GB/VisualBoyAdvance.exe'

for filename in os.listdir(root_dir):
    print(os.path.splitext(filename)[0])
    with open(os.path.join(batch_dir, os.path.splitext(filename)[0] + '.py'), 'w') as OPATH:
        OPATH.writelines(['import subprocess\n\n',
                          'subprocess.Popen(["' + emu + '",',
                          '"' + root_dir + filename + '"',
                          '])'
                          ])
