import os
import subprocess

root_dir = 'C:/Users/ZLHys/ROMs/NES/'
batch_dir = 'C:/Users/ZLHys/ROMs/NES/bats/'
for filename in os.listdir(root_dir):
    print(os.path.splitext(filename)[0])
    with open(os.path.join(batch_dir, 'NES - '+ os.path.splitext(filename)[0] + '.py'), 'w') as OPATH:
        OPATH.writelines(['import subprocess\n\n',
                          'subprocess.Popen(["C:/Users/ZLHys/ROMs/NES/EMU/nestopia.exe",',
                          '"' + root_dir + filename + '"',
                          '])'
                          ])
