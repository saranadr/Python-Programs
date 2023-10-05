'''Write a package named "Food" with below details
 Food/fruit.py
  Declare myfruits list with some fruit names such as
  apple, orange, etc.
  Declare showFruits() function which will
  display all the fruits in for loop.

 Food/vegetable.py
  Declare myvegetables list with some vegetable names such as
  carrot, tomato, etc.
  Declare showVegetables() function which will display
  all the vegetables in for loop.

 Food/snacks.py
  Declare mysnacks list with some snacks names such as
  biscuit, chocolate, etc.
  Declare showSnacks() function which will display
  all the snacks in for loop.
 
 Food/__init__.py
  Import snacks module
  Import showVegetables() function from vegetable module
  Import all variables and functions from fruits module
  
 Import the Food package and check the access level
 for variables and functions. (Direct & Sub-level)
  - Print all the variables (myfruits, myvegetables & mysnacks)
  - Call all the functions  (showFruits, showVegetables & showSnacks)
'''

import food
print(food.fruit.myfruits)
print(food.myfruits)
print('-------')
print(food.vegetable.myveg)
#print(food.myveg)
print('-------')
print(food.snacks.mysnacks)
#print(food.mysnacks)
print('-------')
food.fruit.showfruits()
food.showfruits()
print('-------')
food.vegetable.showveg()
food.showveg()
print('-------')
food.snacks.showsnacks()
#food.showsnacks()
