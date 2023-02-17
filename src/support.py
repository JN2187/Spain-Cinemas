import pandas as pd
import numpy as np
import re
from unicodedata import normalize

def sleep_(n1, n2, n3):
    """Random number generator, suitable for sleeps to scrape
    Args:
        n1 (int, optional): the minimum number it can return.
        n2 (int, optional): the maximum number it can return.
        n3 (int, optional): the number of decimal places returned.
    Returns:
        int: random int between the first number and the second with the third number of decimal places.
    """
    return round(np.random.randint(n1,n2) + np.random.rand(1)[0], n3)

def pick_in_two(lst,num):
    processed_list = [] # Create an empty list to store the processed elements
    for i in range(0, len(lst), num): # Loop through the list with a step of 2
        s = lst[i].lower() # Convert the current element to lowercase
        s = re.sub( # Replace diacritic characters in the string using a regular expression
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
            normalize( "NFD", s), 0, re.I
        )
        s = normalize( 'NFC', s) # Normalize the string to the NFC form
        s = s.replace(' ', '-') # Replace spaces with -
        processed_list.append(s) # Append the processed element to the list
    return processed_list # Return the processed list

    