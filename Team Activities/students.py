'''
Team Activity (Week 9): CSV Files and Dictionaries
CSE 111-07
Nicholas Wilkins 
03/06/2024
'''
import csv

def main():
    # Establish the primary key index for the dictionary
    KEY_INDEX = 0

    # Create the student compound dictionary 
    students_dict = read_dictionary('students.csv', KEY_INDEX)

    print('Welcome to Student Information Search!')

    user_continue = True
    while user_continue != False:
        student_search(students_dict)
        user_continue_input = input('Would you like to search for another student? (yes or no): ')
        if user_continue_input.lower() == 'no':
            user_continue = False
        else:
            user_continue = True
    print('\nThank you, have a great day!\n')
        

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
                
def student_search(dictionary):
    '''
    Searches for student information based on a 9-digit student number.

    Args:
        dictionary (dict): A dictionary containing student information.
            The keys are 9-digit student numbers (as strings), and the values
            are lists with student ID and student name.

    Returns:
        None: Displays student information or error messages.
    '''
    valid = False
    while valid != True:
        user_query = input('\nPlease enter the 9-digit student number, without dashes: ')
        if len(user_query) != 9 or not user_query.isdigit():
            valid = False
            print('\nI am sorry, the information you provided is invalid, please try again!\n')
        else:
            valid = True
            if user_query in dictionary:
                result = dictionary[user_query]
                print('\nStudent Information: ')
                print(f'\nStudent ID: {result[0]}\nStudent Name: {result[1]}\n')
            else:
                print('\nI am sorry, the student information requested is not in the directory, please try again!\n')

if __name__ == "__main__":
    main()