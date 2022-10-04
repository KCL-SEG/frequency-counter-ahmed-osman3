"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        
        #Check if frequencies contains item in string form
        if(frequencies.keys().__contains__(str(item))):
            #Update count of value by 1.
            value = frequencies[str(item)]
            frequencies[str(item)] = value + 1
        else:
            #If value key and value is not present, add new key value to dictionary
            frequencies[str(item)] = 0

    return frequencies

