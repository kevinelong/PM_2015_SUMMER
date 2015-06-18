#Write a program that prints the integers from 1 to 100. But for multiples
#of three print "Fizz" instead of the number, and for the multiples of five
#print "Buzz". For numbers which are multiples of both three and five print
#"FizzBuzz".

def fizzbuzz():
  numbers = range(1, 101)
  for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
      print 'fizzbuzz'
    elif num % 3 == 0:
      print 'fizz'
    elif num % 5 == 0:
      print 'buzz'
    else:
      print num

fizzbuzz()


