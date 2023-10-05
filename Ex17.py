'''Write a program to display below details.
    Logged in User: <username>
    Server Name: <hostname>
    IP Address: <ip-address>
    Current Directory: <current-directory>
    Current Date: <DD-MON-YYYY>
    System Date: Saturday, September 25, 2016 00:00:00 AM PDT
'''
import os
import time
import socket
import getpass
getpass.getuser()
os.chdir('/Users/saraathipatla/Desktop')
#print('Logged in User:',os.getlogin())
#print('Logged in User:',os.path.expanduser('~'))
#print('Logged in User:',os.environ.get('USERNAME'))
print('Logged in User:',getpass.getuser())
print('Server Name:',socket.gethostname())
print('IP Address:',socket.gethostbyname(socket.gethostname()))
print('Current Directory:',os.getcwd())
print('Current Date:',time.strftime("%d/%m/%Y",time.localtime(time.time())))
print('System Date:',os.system('date'))

