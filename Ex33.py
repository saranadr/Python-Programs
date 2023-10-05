'''Write a program to calculate the Celsius to Fahrenheit & vice versa.
(using functions)
 Input:
  Heat Calculator
  ***************
   1. Celsius to Fahrenheit
   2. Fahrenheit to Celsius
  Choose your option [1-2]: 1 
  Enter the celsius: 5
 Output:
  Celsius: 5
  Fahrenheit: 41
'''
def CtoF():
    cel=int(input('Enter the Temperature in Celsius: '))
    far=(cel*9/5)+32
    print('Celsius: {0}\nFahrenheit: {1}'.format(cel,far))

def FtoC():
    far=int(input('Enter the Temperature in Farenheit: '))
    cel=(far-32)*5/9
    print('Fahrenheit: {0}\nCelsius: {1}'.format(far,cel))

#while True:
print('''Heat Calculator
***************
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius''')
op=input('Choose your option [1-2]: ')
if op=='1':
    CtoF()
elif op=='2':
    FtoC()
else:
    print('Invalid option')
    #pass
        
