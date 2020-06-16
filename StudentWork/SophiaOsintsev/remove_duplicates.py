# My solution to remove duplicates from a list
def remove_duplicates():
    l = [1, 2, 3, 4, 3, 4, 9, 5, 2, 6, 'me', 6, 7, 8, 0]
    numbers = list(set(l))
    numbers.sort(key=l.index)
    return numbers

print remove_duplicates()

# My attempt to test time performance:
import time

def remove_duplicates():
    l = range(1, 10000)
    numbers = list(set(l))
    numbers.sort(key=l.index)
    return numbers
start = time.time()
remove_duplicates()
end = time.time()
print 'Time to execute: ', end - start
