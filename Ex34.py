'''
Write a program to calculate the below math formulas.
(using functions)
 Area of square (a*a)
 Area of circle (PI * r*r)
 Area of Triangle (1/2 * b*h)
 Area of Rectangle (w * h)
'''
def square():
    side=float(input('Enter the length of the square: '))
    area=side*side
    print('The area of the square is',area)

def circle():
    rad=float(input('Enter the radius of the circle: '))
    area=3.14*rad*rad
    print('The area of the circle is',area)

def triangle():
    base=float(input('Enter the base of the triangle: '))
    height=float(input('Enter the height of the triangle: '))
    area=1/2*base*height
    print('The area of the triangle is',area)

def rectangle():
    width=float(input('Enter the width of the rectangle: '))
    height=float(input('Enter the height of the rectangle: '))
    area=width*height
    print('The area of the rectangle is',area)

while True:
    print('''What do you want to find the area for
1.Square
2.Circle
3.Triangle
4.Rectangle ''')
    option=input('type the right option: ')
    if option=='1':
        square()
    elif option=='2':
        circle()
    elif option=='3':
        triangle()
    elif option=='4':
        rectangle()
    else:
        print('Invalid option')
        break
    
