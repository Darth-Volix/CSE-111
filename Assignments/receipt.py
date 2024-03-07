'''
03/06/2024
CSE 111-07
Nicholas Wilkins 
Assignment 9:
Text File Receipt Generator
'''
import csv

def main():
    # Establish the indexes that will be used in the program
    KEY_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    QUANTITY_INDEX = 1
    PRICE_INDEX = 2

    # Create the product compound dictionary 
    products_dict = read_dictionary('products.csv', KEY_INDEX)

    # Print the dictionary 
    print(products_dict)
    
    # Open the 'request.csv' file in read mode ('rt')
    with open('request.csv', 'rt') as csv_file:
       
        # Create a CSV reader object
        reader = csv.reader(csv_file)
       
        # Print a header for the requested items
        print('\nRequested Items:')
       
        # Skip the first row (header row) of the CSV file
        next(reader)

        # Iterate through each row in the CSV file
        for row_list in reader:

            # Check if the row is not empty
            if len(row_list) != 0:

                 # Extract relevant information from the row
                key = row_list[KEY_INDEX]
                quantity = row_list[QUANTITY_INDEX]
                product = products_dict[key]
                product_name = product[PRODUCT_NAME_INDEX]
                product_price = product[PRICE_INDEX]

                # Print the product name, quantity, and price
                print(f'{product_name}: {quantity} @ ${product_price}')


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

if __name__ == "__main__":
    main()