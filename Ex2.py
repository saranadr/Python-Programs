'''Declare 3 variables and display message as below using 4 methods (, + % format)
    a=10; b=20.5; name='abcd'
   Output:
    The value of 'a' is 10 and "b" is 20.5 and name is "abcd"
    '''
a=10
b=20.5
name='abcd'
print("The value of 'a' is",a,'and "b" is',b, 'and name is "',name,'"')
print('The value of \'a\' is '+str(a)+' and "b" is '+str(b)+ ' and name is "'+name+'"')
print('The value of \'a\' is %d and "b" is %.1f and name is "%s"'%(a,b,name))
print('The value of \'a\' is {0} and "b" is {1} and name is "{2}"'.format(a,b,name))
