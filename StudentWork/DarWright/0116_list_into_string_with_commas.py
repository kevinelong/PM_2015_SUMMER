def string_together(list):

   one_word = ""
   for word in list:
       if word == list[-1] and len(list) > 1:
           one_word = one_word + " and " + word
       elif word == list[0]:
           one_word = word
       else:
           one_word = one_word + ", " + word
   return one_word

print string_together(["Ollie", "Dar", "Sarah", "Paul"])
print string_together(["Ollie", "Dar"])
print string_together(["Ollie"])