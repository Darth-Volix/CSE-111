'''
Team Activity (Week 2): Store Discount
CSE 111-07
Nicholas Wilkins 
01/17/2024
'''
# Import the datetime class from the datetime module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current date and time as a datetime object from the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Remember, Monday is assigned the integer 0 and it goes up through the week from there. 
# Ask the user for their subtotal at the store today 
user_subtotal = float(input('\nWhat is your subtotal today?: $'))

# Use if/else statement to determine whether or not there is a discount to be given to the customer today.
if day_of_week == 1 or day_of_week == 2 and user_subtotal >= 50:
    # User qualified for a discount based on the day of the week and subtotal amount
    discount_amount = user_subtotal * 0.10
    discounted_price = user_subtotal - discount_amount
    sales_tax = discounted_price * 0.06
    price_with_tax = discounted_price + sales_tax
    print('\nCongratulations! You qualify for a 10 percent discount on your subtotal today!')
    print(f'Here is the total cost breakdown: \n\nTotal Discount: ${discount_amount:.2f}\nDiscounted Subtotal: ${discounted_price:.2f}\nTotal Tax (after discount): ${sales_tax:.2f}\nTotal Cost: ${price_with_tax:.2f}\n\nHave a great day!\n')
else:
    # User did not qualify for a discount based on the day of the week or the subtotal
    sales_tax = user_subtotal * 0.06
    price_with_tax = user_subtotal + sales_tax
    print(f'\nYou do not qualify for a discount today. Here is the total cost breakdown: \n\nTotal Tax: ${sales_tax:.2f}\nTotal Price: ${price_with_tax:.2f}\n\nHave a great day!\n')