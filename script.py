# Write a function that takes a list of integers and returns a new list with each integer squared.
def square_integers(int_list):
    """
    Takes a list of integers and returns a new list with each integer squared.

    Parameters:
    int_list: A list of integers.

    Returns:
    A new list containing the squares of the integers from the input list.
    """
    return [x ** 2 for x in int_list]