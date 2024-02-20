'''
Team Activity (Week 7): Lists
CSE 111-07
Nicholas Wilkins 
02/19/2024
'''
import random

def append_random_numbers(numbers_list, quantity=1):
    '''
    Appends random numbers to the given list.

    Parameters:
        numbers_list (list): The list to which random numbers will be appended.
        quantity (int, optional): The number of random numbers to append. Defaults to 1.

    Returns:
        None
    '''
    for i in range(quantity):
        quantity = random.uniform(0, 1000)
        rounded = round(quantity, 1)
        numbers_list.append(rounded)

def append_random_words(words_list, quantity=1):
    '''
    Appends random words to the given list.

    Parameters:
        words_list (list): The list to which random words will be appended.
        quantity (int, optional): The number of random words to append. Defaults to 1.

    Returns:
        None
    '''
    random_words = ["scream", "beneficial", "waiting", "lackadaisical", "puny", "march", "key", "guide", "swim", "abnormal", "coherent", "afraid", "dote", "ascertain", "saturnine"]
    for i in range(quantity):
        word = random.choice(random_words)
        words_list.append(word)


def main():
    # set up the initial numnbers and words list
    numbers = [13.3, 15.7, 87.3, 100.3, 98.7]
    words = ['Jake', 'snake', 'rake']

    print(f'Numbers: {numbers}')

    # call the append_random_numbers function to add a random number
    append_random_numbers(numbers)

    print(f'Numbers: {numbers}')

    # call the append_random_numbers function to add a specified number of numbers to the list 
    quantity = int(input('How many numbers should be added to the list?: '))
    append_random_numbers(numbers, quantity)

    print(f'Numbers: {numbers}')
    print(f'Words: {words}')

    # call the append_random_words function
    append_random_words(words)

    print(f'Words: {words}')

    # call the append_random_words function to add a specified number of words to the list 
    word_quantity = int(input('How many words should be added to the list?: '))
    append_random_words(words, word_quantity)

    print(f'Words: {words}')

# If this file was executed like this:
# > python random_numbers.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()