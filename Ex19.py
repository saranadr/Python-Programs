'''
19. Write a program to create file inside given directory.
    Input:
     Enter the directory name: MYFOLDER
     Enter the filename      : myfile.txt
     Enter the file content  :
      This is first line
      My second
      line

    Output:
     Current directory:  <path>
     Files in directory: <files-list>
     Folder created successfully.
     File created successfully.
     Contents inside file: <contents-of-file>
'''
import os
import sys
os.chdir('/Users/saraathipatla/Desktop')
def readfile():
    fp = open(fname, 'r')
    for line in fp:
        print(line, end='')
    fp.close()

def writefile():
    fp=open(fname,'w')   
    print('Enter the file content  :')
    content=sys.stdin.readlines()
    fp.writelines(content)
dname=input('Enter the directory name:') #how to check if folder is already there
os.mkdir(dname)
os.chdir(os.getcwd()+'/'+dname)
fname=input('Enter the filename      :') 
writefile()
print('Current directory:',os.getcwd())
print('Files in directory:',os.listdir('.')) #listdir is not working for desktop
print('Folder created successfully.')
print('File created successfully.')
print('Contents inside file:')
readfile()
