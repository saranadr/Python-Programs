'''Write a program to parse the below sales data and display below output.
  Data:
  #product;,;price;,;PurchaseDate
  sales_data = """ 
   Biscuit ;,;  $20.5  ;,;  01/07/2021  ,    Apple     ;,;
    $10.0;,;     02/07/2021, Snacks;,;  $30.4  ;,;   03/07/2021
  ,    BISCUIT   ;,;  $10.5     ;,;  04/07/2021      ,
  snacks      ;,;     $10.6;,;     05/07/2021
"""
  Output:
    ***** Sales Details *****
    apple(1)    -> $10.0
    biscuit(2)  -> $31.0
    snacks(2)   -> $41.0'''

##data='#product;,;price;,;PurchaseDate'
##data=data.replace('#','').replace(';,;',',').split(',')
sales_data=""" 
   Biscuit ;,;  $20.5  ;,;  01/07/2021  ,    Apple     ;,;
    $10.0;,;     02/07/2021, Snacks;,;  $30.4  ;,;   03/07/2021
  ,    BISCUIT   ;,;  $10.5     ;,;  04/07/2021      ,    snacks      ;,;     $10.6;,;     05/07/2021
"""
sales_data=sales_data.replace(';,;',':').replace('\n','').replace('$','').replace(' ','').split(',')
product={}
for i in sales_data:
    i=i.lower()
 #   i=i.split(':')
    (pname,price)=i.split(':')
    if i[0] not in product.keys():
        product.update({i[0]:[float(i[1]),1]})
    else:
        product[i[0]][0]+=float(i[1])
        product[i[0]][1]+=1
print('***** Sales Details *****')
for i in sorted(product):
    print('{0}({2}) --> ${1}'.format(i,product[i][0],product[i][1]))
    
