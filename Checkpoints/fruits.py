def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    # Reverse the list
    fruit_list.reverse()

    # Print the list
    print(f'reversed: {fruit_list}')

    # Add orange to the list
    fruit_list.append('Orange')

    # Print the list
    print(f'Appended list: {fruit_list}')

    # Add cherry to the list before apple
    apple_index = fruit_list.index('apple')
    fruit_list.insert(apple_index, 'cherry')

    # Print the list
    print(f'Cherry list: {fruit_list}')

    # Remove banana from the list
    banana_index = fruit_list.index('banana')
    fruit_list.pop(banana_index)

    # Print the list
    print(f'popped list: {fruit_list}')

    # Remove the last element from the list
    popped_fruit = fruit_list.pop()

    # Print the removed element and the list
    print(f'last removed: {fruit_list}')
    print(f'removed fruit: {popped_fruit}')

    # Sort the list
    fruit_list.sort()

    # Print the list
    print(f'sorted list: {fruit_list}')

    # Clear the list
    fruit_list.clear()

    # Print the list
    print(f'cleared list: {fruit_list}')


main()
