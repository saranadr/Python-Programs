def writefile():
    fp = open('sample.txt', 'w')
    #fp = open('C:\\Users\\MEGALADEVI B\\Desktop\\Python\\sample.txt', 'w')
    #fp = open('sample.txt', 'a')
    fp.write('Welcome to python program - 2\n')

    mystr="This is second line\n"
    fp.write(mystr)

    lines = ["Third line\n", "End line\n"]
    fp.writelines(lines)
    
    fp.close()
    print("File created successfully.")

def readfile():
    fp = open('sample.txt', 'r')

    '''
    print("TELL: ", fp.tell())
    mystr = fp.read(5)
    print("MYSTR: ", mystr)
    print("TELL: ", fp.tell())
    fp.seek(0)
    print("TELL: ", fp.tell())

    line = fp.readline()
    print("LINE: ", line)
    
    lines = fp.readlines()
    print("LINES:", lines)
    
    '''
    for line in fp:
        print(line, end="")
    fp.close()

#writefile()
readfile()

