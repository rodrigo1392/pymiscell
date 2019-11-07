""" Functions to be used by a Python 3 interpreter.
    Developed by Rodrigo Rivero.
    https://github.com/rodrigo1392"""

import re


def letters_list(start_char='A', end_char='Z', capitalize=True):
    """
    Generates a list of alphabetically order english letters.
    It can go beyond Z, with AA, AB,... format
    Inputs: start_char. Character to start from. 
            end_char. Last character on the list. 
            capitalize. Boolean. If True, output are capital letters 
    Output: List of character strings. 
    """
    import string
    base_list = [i for i in string.ascii_lowercase]
    for i in base_list:
        base_list = base_list + [i + c for c in string.ascii_lowercase]
    output_list = base_list[base_list.index(start_char.lower()):
                            base_list.index(end_char.lower()) + 1]
    if capitalize is True:
        output_list = [c.upper() for c in output_list]
    return output_list


def sort_strings_by_digit(strings_list):
    """
    Returns a by-digits-sorted version of input strings_list. If digits are not present on the strings,
    then returns the original input strings_list without changes.
    Input: strings_list. List of strings to be sorted.
    Output: List of sorted strings.
    """
    try:
        numbers = [int(re.findall(r'-?\d+\.?\d*', i)[-1].replace('.', '')) for i in strings_list]  # Extract integers
        sorted_list = [x for _, x in sorted(zip(numbers, strings_list))]  # Sort input strings_list by integers
    except IndexError:  # Catch no digits error
        sorted_list = strings_list
        print('WARNING: FILES LIST NOT SORTED BY NUMBER')
    return sorted_list


def str_check_if_has_numbers(input_string):
    """
    Return boolean True if the input_string has a digit on it, False otherwise.
    Input: input_string: String to be checked.
    Output: Boolean.
    """
    return any(char.isdigit() for char in input_string)


def str_list_2command_line(input_list):
    """
    Transforms a list into a string, to pass it in a command line.
    Input: input_list. List of strings to be joined.
    Output: Command like string to be passed as command option.
    """
    return "['" + "', '".join(input_list) + "']"
