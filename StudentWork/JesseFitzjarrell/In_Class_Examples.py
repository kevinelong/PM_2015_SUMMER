__author__ = 'lenny'
# exercises that we work on in class. Kind of a playbox if you will
# Jesse Fitzjarrell

# remove duplicates from a list
def remove_duplicates(values):
    # defined a class  called remove_duplicates and pushed a function called values through it
    output = []
    # created the output list
    seen = set()
    # created the seen set and put it into the empty set
    for value in values:
        #looping through the values
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            #looks at all the values in the values list
            output.append(value)
            #looks to see what is similar in the list
            seen.add(value)
            #returns the new list without duplicates
    return output

# Remove duplicates from this list.
values = [5, 5, 1, 1, 2, 3, 4, 4, 5]
# runs the result method to remove the dulplicates
result = remove_duplicates(values)
# print the results
print(result)

