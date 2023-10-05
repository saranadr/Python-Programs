import sys
print("Command line args:", sys.argv)

def add(x, y):
    print("Args: ", x, y)
    print("Addition: ", x + y)

#add(10, 20)
add(int(sys.argv[1]), int(sys.argv[2]))
