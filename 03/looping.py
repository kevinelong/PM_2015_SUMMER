import random
import time


# Examples of how to use while and for
count = 1
while count < 10:
    print count, 'Reina'
    count += 1
else:
    print 'Pamina'


for x in range(10):
    if x > 5:
        continue
    print x, 'Reina'
else:
    print 'Pamina'


while True:
    for x in range(10):
        if x > 5:
            break
        print x, 'Pamina'
    print 'Reina'


# sample answers to challenges
def random_numbers_for_given_length_of_time(length):
    start = time.time()
    end = start + length
    while time.time() < end:
        print random.randrange(100)
    msg = (
        'I just printed random numbers for '
        '{} seconds!'.format(length)
    )
    print msg

random_numbers_for_given_length_of_time(5)
