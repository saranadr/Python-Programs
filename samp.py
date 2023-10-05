# Define the sales data
sales_data = """ 
 Biscuit ;,;  $20.5  ;,;  01/07/2021  ,    Apple     ;,;
  $10.0;,;     02/07/2021, Snacks;,;  $30.4  ;,;   03/07/2021
,    BISCUIT   ;,;  $10.5     ;,;  04/07/2021      ,    snacks      ;,;     $10.6;,;     05/07/2021
"""

# Initialize a dictionary to store sales data for each product
sales = {}

# Split the sales data by ',' and ';'
sales_list = [entry.strip() for entry in sales_data.split(",;")]

# Process the sales data
for i in range(0, len(sales_list), 3):
    product = sales_list[i].lower()
    price = float(sales_list[i + 1].replace('$', '').strip())
    if product in sales:
        sales[product] += price
    else:
        sales[product] = price

# Display the sales details
print("***** Sales Details *****")
for product, total_sales in sales.items():
    print(f"{product.capitalize()}({sales_list.count(product)}) -> ${total_sales:.1f}")
