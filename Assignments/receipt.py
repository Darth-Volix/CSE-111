'''
03/06/2024
CSE 111-07
Nicholas Wilkins 
Assignment 9:
Text File Receipt Generator
'''
import csv
from datetime import datetime
import random

def main():
    # Establish the indexes that will be used in the program
    KEY_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    QUANTITY_INDEX = 1
    PRICE_INDEX = 2

    try:
        # Create the product compound dictionary 
        products_dict = read_dictionary('products.csv', KEY_INDEX)

        # Open the 'request.csv' file in read mode ('rt')
        with open('request.csv', 'rt') as csv_file:
        
            # Create a CSV reader object
            reader = csv.reader(csv_file)

            # Print a header for the requested items
            print('\nInkom Emporium\n')

            # Set the total items and subtotal price to 0
            total_items = 0
            subtotal = 0

            # Skip the first row (header row) of the CSV file
            next(reader)

            # Iterate through each row in the CSV file
            for row_list in reader:

                # Check if the row is not empty
                if len(row_list) != 0:

                     # Extract relevant information from the row
                    key = row_list[KEY_INDEX]
                    quantity = int(row_list[QUANTITY_INDEX])
                    product = products_dict[key]
                    product_name = product[PRODUCT_NAME_INDEX]
                    product_price = float(product[PRICE_INDEX])

                    total_items += quantity
                    subtotal += product_price

                    # Print the product name, quantity, and price
                    print(f'{product_name}: {quantity} @ ${product_price}')

            # Compute the sales tax
            sales_tax = compute_sales_tax(subtotal)

            # Compute the total price
            total_price = compute_total(subtotal, sales_tax)

            # Print out the item totals and price totals    
            print(f'\nNumber of items: {total_items}')
            print(f'Subtotal: ${subtotal}')
            print(f'Sales Tax: ${sales_tax}')
            print(f'Total: ${total_price}\n')

            # Get the current date and time
            current_datetime = datetime.now()

            # Format the date and time
            formatted_datetime = current_datetime.strftime('%a %b %d %H:%M:%S %Y')

            # Print the date and time
            print('Thank you for shopping at the Inkom Emporium.')
            print(formatted_datetime)

            # Print the coupon
            print('\n- - - - - - - - - - - - - - - - - - - - - -')
            generate_coupon()
            print('\n- - - - - - - - - - - - - - - - - - - - - -')

    except FileNotFoundError as not_found_err:
        # This code will be executed if the file does not exist
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"Error: The file doesn't exist.")

    except KeyError as key_err:
        # This code will be executed if a vlaue does not exist in the dictionary
        print()
        print(type(key_err).__name__, key_err, sep=": ")
        print("Error: unknown product ID in the request.csv file", key_err)

def read_dictionary(filename, key_index):
    '''
    Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    '''
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, 'rt') as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list

    return dictionary

def compute_sales_tax(subtotal):
    '''
    Calculate the sales tax for a given subtotal.

    This function computes the sales tax at a fixed rate of 7.5% on the subtotal
    of a purchase. The tax amount is rounded to two decimal places.

    Parameters:
    subtotal (float): The total amount before tax.

    Returns:
    float: The amount of sales tax for the given subtotal.
    '''
    sales_tax = round(subtotal * 0.075, 2)
    
    return sales_tax

def compute_total(subtotal, sales_tax):
    '''
    Calculate the total price including sales tax.

    This function adds the sales tax to the subtotal of a purchase and rounds the result to two decimal places to compute the total price.

    Parameters:
    subtotal (float): The total amount before tax.
    sales_tax (float): The amount of sales tax to be added.

    Returns:
    float: The total price after adding sales tax.
    '''
    total_price = round(subtotal + sales_tax, 2)
    
    return total_price

def generate_coupon():
    '''
    Generates a random discount coupon for Inkom Emporium.

    This function selects a random discount percentage from a predefined list of discounts,
    creates a unique coupon code, and prints out an exclusive offer message with the
    discount and coupon code.

    Discounts available: 10%, 20%, 25%, 30%, 50%.

    Returns:
        None: This function does not return any value. It prints the coupon details directly.
    '''
    discounts = ['10%', '20%', '25%', '30%', '50%']
    discount = random.choice(discounts)
    coupon_code = 'INK' + str(random.randint(100, 999))

    print(f"***Inkom Emporium Exclusive Offer***\n")
    print(f"Congratulations! You've received a {discount} \ndiscount on your next purchase.")
    print(f"\nUse the coupon code: {coupon_code} at checkout.")

if __name__ == "__main__":
    main()