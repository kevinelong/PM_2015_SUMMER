def is_prime(num):
    for x in xrange(2, num-1):
        if num % x == 0:
            return False

# Can't put 2 or 3 in there right now because the range gets messed up. Could expand to include them as
# special cases. :)

print is_prime(3)
print is_prime(15)