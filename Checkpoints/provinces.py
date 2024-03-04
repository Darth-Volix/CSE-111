'''
Checkpoint 9: Working With Text Files
CSE 111-07
Nicholas Wilkins 
03/04/2024
'''

def main():
    # Call the create_list function to create a list of provinces from a text file and then
    # print that list
    province_list = create_list("provinces.txt")
    print(province_list)

    # Call the remove_element function to remove the first and last elements from the list 
    # and store the list in memory
    remove_elements(province_list)

    # Call the replace_elements function to replace all items in the list that are "AB" to
    # "Alberta" and store the list in memory 
    replace_elements(province_list)

    # Call the count_elements function to count the number of times "Alberta" appears in 
    # the list and print it out
    element_count = count_elements(province_list)
    print(f'\nAlberta occurs {element_count} times in the modified list, which is printed below.\n')

    # Print the final result
    print(province_list)


def create_list(filename):
    '''
    Reads a text file and returns its contents as a list of cleaned lines.

    Parameters:
        filename (str): The name of the text file to read.

    Returns:
        list (list): A list containing the cleaned lines from the file.

    Example:
        >>> create_list("my_file.txt")
        ['This is line 1.', 'And this is line 2.', 'Line 3 follows.']
    '''
    list = []
    with open(filename, "rt") as file_text:
        for line in file_text:
            clean_line = line.strip()
            list.append(clean_line)
    return list

def remove_elements(list):
    '''
    Removes the first and last elements from the given list.

    Parameters:
        list (list): The list from which to remove elements.

    Returns:
        list (list): A new list with the first and last elements removed.

    Example:
        >>> my_list = [1, 2, 3, 4, 5]
        >>> remove_elements(my_list)
        [2, 3, 4]

    Note:
        This function modifies the original list by removing elements in-place.
    '''
    list.pop(0)
    list.pop(-1)
    return list

def replace_elements(list):
    '''
    Replaces occurrences of 'AB' with 'Alberta' in the given list.

    Paramters:
        list (list): The list in which to perform replacements.

    Returns:
        list (list): A modified list with 'AB' replaced by 'Alberta'.

    Example:
        >>> my_list = ['AB', 'BC', 'AB', 'SK']
        >>> replace_elements(my_list)
        ['Alberta', 'BC', 'Alberta', 'SK']
    '''
    for i in range(len(list)):
        if list[i] == 'AB':
            list[i] = 'Alberta'
    return list

def count_elements(list):
    '''
    Counts the occurrences of 'Alberta' in the given list.

    Parameters:
        list (list): The list to search for occurrences.

    Returns:
        element_count (int): The number of times 'Alberta' appears in the list.

    Example:
        >>> my_list = ['Alberta', 'BC', 'Alberta', 'SK', 'Alberta']
        >>> count_elements(my_list)
        3
    '''
    element_count = 0 
    for i in range(len(list)):
        if list[i] == "Alberta":
            element_count += 1
    return element_count

if __name__ == "__main__":
    main()