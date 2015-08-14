import sys
import os
try:
    from .models import Pet
except ValueError:  # this is being run from command line and these imports did not work
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    sys.path.append('/Users/rachel/Projects/PM_2015_SUMMER/StudentWork/RachelKlein/mysite')
    from petlibrary.models import Pet

if __name__ == '__main__':
    choice = raw_input("Which pet would you like to play with today? Enter 1 to search for a pet by name or 2 for a list of all pets. >> ")
    if choice == "1":
        pet_name = raw_input("Okay, what's the name of the pet you'd like to play with? >> ")
        chosen_pet, created = Pet.objects.get_or_create(name=pet_name)
        print "Of course you can play with " + chosen_pet.name + "!"
    elif choice == "2":
        current_pets = Pet.objects.all()
        for pet in current_pets:
            print "Press " + str(pet.id) + " to play with " + pet.name
        chosen_pet = raw_input()