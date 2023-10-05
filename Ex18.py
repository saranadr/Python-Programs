'''
Write a program to get file name as input from user and display properties of a file.
    Input:
     Enter the filename:  sample.txt
    Output:
     Given filename: sample.txt
     ***** File Properties *****
     File Exist: True
     Is File   : True
     File Size : 20
     Created Time: <date>
     File Content: <contents of the file here>
'''
#in idle, this worls for files created using python. so run Ex19.py and then run nEx18.py
import os
os.chdir('/Users/saraathipatla/Desktop/MYFOLDER')
fname=input('Enter the filename: ')
print('Given filename:',fname)
print('***** File Properties *****')
print('File Exist:',os.path.exists(fname))
print('Is File   :',os.path.isfile(fname))
print('File Size :',os.path.getsize(fname))
print('Created Time:',os.path.getctime(fname))
def readfile():
    fp = open(fname, 'r')
    for line in fp:
        print(line, end="")
    fp.close()
print('File Content:')
readfile()

