with open('/Users/purple4reina/Desktop/class-is-fun.txt', 'wr') as my_file:
    my_file.write('Class is so fun even when the weather is hot\n')


lots_file_path = '/Users/purple4reina/Documents/CodeGuild/PM_2015_SUMMER/lots-of-stuff.txt'
with open(lots_file_path) as lots_file:
    for line in lots_file:
        print line,


my_file = '/Users/purple4reina/name-age.txt'

choice = int(raw_input('Do you want to get (1) or write a name (2)?  '))

if choice == 2:
    name = raw_input('What is your name?  ')
    age = raw_input('What is your age?  ')

    with open(my_file, 'a') as name_age_file:
        name_age_file.write('{},{}\n'.format(name, age))

elif choice == 1:
    name_requested = raw_input('What name are you looking for?  ')
    with open(my_file) as name_age_file:
        for line in name_age_file:
            name, age = line.split(',')
            if name_requested == name:
                print 'The age of {} is {}'.format(name, age)
