'''
01/26/2024
CSE 111-07
Nicholas Wilkins 
Assignment 3:
Turing Test Sentence Generator
'''
# import the random library for use later in the program
import random 

# for clarity on the integers for quantity and tense, the integers mean the following:
# for tense, a 1 means past tense, a 2 means present tense, and a 3 means future tense
# for quantity, a 1 means singular, a 2 means plural

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == 1:
        verbs = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif tense == 2 and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == 2 and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == 3:
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    # randomly choose and return a verb
    verb = random.choice(verbs)
    return verb

# define main program function
def main():
    print('\nWelcome to the Turing Test Sentence Generator!\nThe program will print 6 unique sentences.\n') 
    # program will need to generate 6 sentences
    sentence_count = 1 
    while sentence_count < 7:
        if sentence_count == 1:
            quantity = 1
            tense = 1 
            determiner = get_determiner(quantity)
            noun = get_noun(quantity)
            verb = get_verb(quantity, tense)
            print(f'{determiner.capitalize()} {noun} {verb}.')
            sentence_count += 1
        elif sentence_count == 2:
            quantity = 1
            tense = 2
            determiner = get_determiner(quantity)
            noun = get_noun(quantity)
            verb = get_verb(quantity, tense)
            print(f'{determiner.capitalize()} {noun} {verb}.')
            sentence_count += 1
        elif sentence_count == 3:
            quantity = 1
            tense = 3
            determiner = get_determiner(quantity)
            noun = get_noun(quantity)
            verb = get_verb(quantity, tense)
            print(f'{determiner.capitalize()} {noun} {verb}.')
            sentence_count += 1
        elif sentence_count == 4:
            quantity = 2
            tense = 1
            determiner = get_determiner(quantity)
            noun = get_noun(quantity)
            verb = get_verb(quantity, tense)
            print(f'{determiner.capitalize()} {noun} {verb}.')
            sentence_count += 1
        elif sentence_count == 5:
            quantity = 2
            tense = 2
            determiner = get_determiner(quantity)
            noun = get_noun(quantity)
            verb = get_verb(quantity, tense)
            print(f'{determiner.capitalize()} {noun} {verb}.')
            sentence_count += 1
        elif sentence_count == 6:
            quantity = 2
            tense = 3
            determiner = get_determiner(quantity)
            noun = get_noun(quantity)
            verb = get_verb(quantity, tense)
            print(f'{determiner.capitalize()} {noun} {verb}.')
            sentence_count += 1

# call and run the main function
main()