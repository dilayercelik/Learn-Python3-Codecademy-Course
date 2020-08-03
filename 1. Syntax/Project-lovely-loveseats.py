#adding item 1 description
lovely_loveseat_description = '''
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
'''
print(lovely_loveseat_description)

#adding item 1 price
lovely_loveseat_price = 254.00

#adding item 2
stylish_settee_description = '''
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
'''
print(stylish_settee_description)

#adding item 2 price
stylish_settee_price = 180.50

#ading item 3
luxurious_lamp_description = '''
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
'''
print(luxurious_lamp_description)

#adding item 3 price
luxurious_lamp_price = 52.15


#the sales tax is equal to:
sales_tax = 0.088

#the total amount customer one needs to pay for now
customer_one_total = 0

#what the customer one wants to purchase for now
customer_one_itemization = ""


#customer one purchased item 1
customer_one_total += lovely_loveseat_price
print(customer_one_total)

customer_one_itemization += lovely_loveseat_description
print('For now, the customer one has purchased:', customer_one_itemization)

#customer one purchased item 2 
customer_one_total += luxurious_lamp_price
print(customer_one_total)

customer_one_itemization += luxurious_lamp_description
print('For now, the customer one has purchased:', customer_one_itemization)

#amount of tax for customer one purchase
customer_one_tax = customer_one_total * sales_tax
print('This is the additional amount the customer one needs to pay (tax):', customer_one_tax)

#final total amount of money (after tax) customer one needs to pay
customer_one_total += customer_one_tax
print('This is the total amount the customer one must pay (after tax):', customer_one_total)

#list of all items purchased by customer one
print("Customer One Items:")
print(customer_one_itemization)

