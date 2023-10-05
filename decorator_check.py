def calc(f1, x, y):
    print("Welcome to Calc Function")
    print("Given args: ", x, y)
    f1(x,y)
    
def add(x, y):
    print("Addition: ", x + y)

def mul(x, y):
    #print("Given args: ", x, y)
    print("Multiply: ", x * y)


#add(10, 20)
#mul(10, 20)
calc(add, 10, 20)
calc(mul, 10, 20)  
