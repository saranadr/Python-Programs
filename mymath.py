'''
this is the comment line
tgis is my math module
it contains variables and functions'''

a=100
def add(x,y):
    print('Namespace:',__name__)
    print('addition:',x+y)

if __name__=='__main__':
    print(a)
    add(10,20)
