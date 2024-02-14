'''
Team Activity (Week 6): Self-Esteem Survey
CSE 111-07
Nicholas Wilkins 
02/14/2024
'''
def positive_statement_score(response):
    '''
    Assigns a score based on the user's response to a positive statement.

    Parameters:
        response (str): User's response. Should be one of 'D', 'd', 'a', or 'A'.

    Returns:
        int: A score representing the user's agreement level:
            - 0: Strongly disagrees
            - 1: Disagrees
            - 2: Agrees
            - 3: Strongly agrees
    '''
    if response == 'D':
        # user strongly disagrees
        score = 0
        return score
    elif response == 'd':
        # user disagrees
        score = 1
        return score
    elif response == 'a':
        # user agrees
        score = 2
        return score
    elif response == 'A':
        # user strongly agrees 
        score = 3
        return score
          
def negative_statement_score(response):
    '''
    Assigns a score based on the user's response to a negative statement.

    Parameters:
        response (str): User's response. Should be one of 'D', 'd', 'a', or 'A'.

    Returns:
        int: A score representing the user's disagreement level:
            - 3: Strongly disagrees
            - 2: Disagrees
            - 1: Agrees
            - 0: Strongly agrees
    '''
    if response == 'D':
        # user strongly disagrees
        score = 3
        return score
    elif response == 'd':
        # user disagrees
        score = 2
        return score
    elif response == 'a':
        # user agrees
        score = 1
        return score
    elif response == 'A':
        # user strongly agrees 
        score = 0
        return score
       
def main():
    '''
    Main Function Of The Program
    '''
    # set the score to 0 at the beginning of the 0
    score = 0 

    # begin survey
    print('\nThis program is an implementation of the Rosenberg\nSelf-Esteem Scale. This program will show you ten\nstatements that you could possibly apply to yourself.\nPlease rate how much you agree with each of the\nstatements by responding with one of these four letters:\n')
    print('D means you strongly disagree with the statement.\nd means you disagree with the statement.\na means you agree with the statement.\nA means you strongly agree with the statement.\n')
    response = input('1. I feel that I am a person of worth, at least on an equal plane with others.\n  Enter D, d, a, or A: ') 
    score += positive_statement_score(response)
    response = input('2. I feel that I have a number of good qualities.\n  Enter D, d, a, or A: ')
    score += positive_statement_score(response)
    response = input('3. All in all, I am inclined to feel that I am a failure.\n  Enter D, d, a, or A: ')
    score += negative_statement_score(response)
    response = input('4. I am able to do things as well as most other people.\n  Enter D, d, a, or A: ')
    score += positive_statement_score(response)
    response = input('5. I feel I do not have much to be proud of.\n  Enter D, d, a, or A: ')
    score += negative_statement_score(response)
    response = input('6. I take a positive attitude toward myself.\n  Enter D, d, a, or A: ')
    score += positive_statement_score(response)
    response = input('7. On the whole, I am satisfied with myself.\n  Enter D, d, a, or A: ')
    score += positive_statement_score(response)
    response = input('8. I wish I could have more respect for myself.\n  Enter D, d, a, or A: ')
    score += negative_statement_score(response)
    response = input('9. I certainly feel useless at times.\n  Enter D, d, a, or A: ')
    score += negative_statement_score(response)
    response = input('10. At times I think I am no good at all.\n  Enter D, d, a, or A: ')
    score += negative_statement_score(response)

    # display results
    print(f'\nYour score is {score}.\nA score below 15 may indicate problematic low self-esteem.\n')

# If this file was executed like this:
# > python esteem.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()