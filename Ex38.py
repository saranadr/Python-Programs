'''Write a program to calculate the number of files and
size of all filesin given folder.
  If the directory is not available display an error message
  "MYFOLDER: Directory does not exist".
  Input:
   Enter the folder name: MYFOLDER
  Output:
   Folder Details: (MYFOLDER)
   ***************
   Files:
    abc.txt
    sample.py
    welcome.txt
   Folders:
    mydir1
    mydir2
   Total number of files: 3
   Total number of directories: 2
   Total size of all files: 1405 bytes
'''

import os
folder=input('Enter the folder name: ')
if os.path.isdir(folder)==False:
    print('{0}: Directory does not exist'.format(folder))
else:
    print('Folder Details: ({0})\n***************'.format(folder))
    os.chdir(folder)
    filelist=[]
    folderlist=[]
    size=0
    for i in os.listdir('.'):
#        fname=folder+'/'+i
        if os.path.isfile(i)==True:
            filelist.append(i)
            size+=os.path.getsize(i)
        if os.path.isdir(i)==True:
            folderlist.append(i)

    print('Files:')
    for i in filelist:
        print(i)

    print('Folders:')
    for i in folderlist:
        print(i)
    
    print('Total number of files:',len(filelist))
    print('Total number of directories:',len(folderlist))
    print('Total size of all files: {0}bytes'.format(size))
