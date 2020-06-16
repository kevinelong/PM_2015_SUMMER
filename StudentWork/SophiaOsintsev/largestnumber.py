# Return an array consisting of the largest number from each provided sub-array. For simplicity, the provided
# array will contain exactly 4 sub-arrays.

def largest_number(lists):
# iterate through each sublist
    output = []
    for list in lists:
        output.append(max(list))
    return output
# find largest
# append to output

print largest_number([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]])