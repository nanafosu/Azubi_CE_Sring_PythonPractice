product = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", 
           "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
old_price = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

old_average_price =sum(old_price)/len(old_price)
print('')
print('Total price average for all products: ', old_average_price)
new_price = [price -5 for price in old_price]
print('')
print('New Price List after $5 reduction: ', new_price)
print('')
product_data = {}
revenue_last_week = 0

for i in range(len(product)):
    price = old_price[i]
    quantity = last_week[i]
    revenue = price * quantity
    product_data[product[i]] = (price, quantity, revenue)
    revenue_last_week += revenue

print("Total Revenue Last Week:", revenue_last_week)
print('')
daily_revenue = revenue_last_week/7
print('Average daily Revenue: ',daily_revenue)
print('')

print('Products less than $30 after reduction:')
print('--------------------')
price_dict = dict(zip(product, new_price))

for product, price in price_dict.items():
    if price < 30:
        print(f"{product}: {price}")
print('--------------------')