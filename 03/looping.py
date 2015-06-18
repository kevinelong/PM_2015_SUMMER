import time



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
