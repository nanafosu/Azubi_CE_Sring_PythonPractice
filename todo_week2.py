food_charge = int(input('How much was your food: '))
tip = food_charge * (18/100)
tax_on_food = food_charge * (7/100)

print('Charge for food = $', food_charge)
print('')
print('Tip = $'+ str(tip))
print('')
print('Sales tax = $' + str(tax_on_food))
print('')
print('Grand Total = $' + str(food_charge + tip + tax_on_food))
print('')