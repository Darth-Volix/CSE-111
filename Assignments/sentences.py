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

def get_adjective():
    # randomly select an adjective and return it
    adjectives = ["uncovered", "grieving", "open", "striped", "dangerous", "nasty", "abhorrent", "lyrical", "mammoth", "encouraging", "kaput", "previous", "whimsical", "fierce", "sparkling", "cozy", "vibrant", "mysterious", "playful", "serene", "dazzling", "enchanting", "zesty", "effervescent", "exquisite", "radiant", "tranquil", "resilient", "captivating", "bountiful", "glorious", "bewitched", "charming", "vivacious"]

    adjective = random.choice(adjectives)
    return adjective

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    # randomly choose and return a preposition
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    if quantity == 1:
        prep_noun = get_noun(quantity)
        prep_determiner = get_determiner(quantity)
        preposition = get_preposition()
        prepositional_phrase = (f'{preposition} {prep_determiner} {prep_noun}')
        
        return prepositional_phrase
    elif quantity == 2:
        prep_noun = get_noun(quantity)
        prep_determiner = get_determiner(quantity)
        preposition = get_preposition()
        prepositional_phrase = (f'{preposition} {prep_determiner} {prep_noun}')

        return prepositional_phrase
    
def make_sentence(quantity, tense):
    # call the different functions to retrieve the pieces of the sentence
     determiner = get_determiner(quantity)
     noun = get_noun(quantity)
     verb = get_verb(quantity, tense)
     adjective = get_adjective()
     prepositional_phrase = get_prepositional_phrase(quantity)
     
     # assemble the pieces into a full sentence
     sentence = print(f'{determiner.capitalize()} {adjective} {noun} {verb} {prepositional_phrase}.')

     return sentence
                                
# define main program function
# for clarity on the integers for quantity and tense, the integers mean the following:
# for tense, a 1 means past tense, a 2 means present tense, and a 3 means future tense
# for quantity, a 1 means singular, a 2 means plural

def main():
    # program will ask if the user would like to generate sentences, close if they do not, and have the user retry if there is an invalid input
    # output is taken into consideration, using empty print() statements in a couple places to make the output visually appealing on screen
    print('\nWelcome to the Sentence Generator!\n') 
    generate_sentences = True
    while generate_sentences != False:
        sentence_count = 1
        user_continue = input('Generate Sentences? (yes or no): ')
        if user_continue.lower() == 'yes':
            generate_sentences = True
            while sentence_count < 7:
                if sentence_count == 1:
                    print()
                    make_sentence(1, 1)
                    sentence_count += 1
                elif sentence_count == 2:
                    make_sentence(1, 2)
                    sentence_count += 1
                elif sentence_count == 3:
                    make_sentence(1, 3)
                    sentence_count += 1
                elif sentence_count == 4:
                    make_sentence(2, 1)
                    sentence_count += 1
                elif sentence_count == 5:
                    make_sentence(2, 2)
                    sentence_count += 1
                elif sentence_count == 6:
                    make_sentence(2,3)
                    print()
                    sentence_count += 1
        elif user_continue.lower() == 'no':
            generate_sentences = False
            print('\nThank you. Goodbye.\n')
        else:
            print('\nInput is invalid, please try again!\n')
        
# call and run the main function
main()