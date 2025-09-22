# Write a program that converts a Roman numeral to an integer.
def roman_to_integer(roman):    
    """
    Converts a Roman numeral to an integer.

    Parameters:
    roman: A string representing the Roman numeral.

    Returns:
    An integer corresponding to the Roman numeral.
    """
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total