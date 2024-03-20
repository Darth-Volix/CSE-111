import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    # Read student data from 'pupils.csv' file
    students_list = read_compound_list('pupils.csv')

    # Define a lambda function to extract birthdate from student data
    birthdate_func = lambda student: student[BIRTHDATE_INDEX]

    # Define a lambda function to extract the birthdate based on month and day 
    birthdate_func2 = lambda student: student[BIRTHDATE_INDEX][5:]

    # Defin a lambda function to extract the given name from the student data 
    name_func = lambda student: student[GIVEN_NAME_INDEX]

    # Sort the student list based on birthdate using the lambda function
    sorted_list = sorted(students_list, key=birthdate_func)

    # Sort the student list based on given name
    sorted_list2 = sorted(students_list, key=name_func)

    # Sort the student list based on the month and day rather than the year
    sorted_list3 = sorted(students_list, key=birthdate_func2)

    # Print the sorted student list
    print_list(sorted_list)
    print()

    # Print the second sorted student list 
    print_list(sorted_list2)
    print()

    # Print the third sorted student list
    print_list(sorted_list3)
    print()


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(list):
    '''
    Prints each element in the given list.

    Args:
        my_list (list): The list of elements to be printed.

    Returns:
        None
    '''
    for element in list:
        print(element)
    print()


if __name__ == "__main__":
    main()