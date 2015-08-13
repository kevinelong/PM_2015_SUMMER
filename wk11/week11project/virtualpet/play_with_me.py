import sys
import os

try:
    from .models import Animal, list_to_comma
    from .exceptions import DeathException, RunAwayException
except ValueError:  # this is being run from command line and these imports did not work
    os.environ['DJANGO_SETTINGS_MODULE'] = 'week11project.settings'
    sys.path.append('/Users/purple4reina/Documents/CodeGuild/PM_2015_SUMMER/wk11/week11project')

    from virtualpet.models import Animal, list_to_comma
    from virtualpet.exceptions import DeathException, RunAwayException

import asciiart


pet_type = raw_input(
    'Welcome to the pet store! What type of animal would '
    'you like?  '
).title()
name = raw_input('What is your new pet\'s name?  ').title()

# create the pet object
try:
    pet = globals().pop(pet_type).objects.get_or_create(name=name)
except KeyError:
    pet = Animal.objects.create(name=name)

while True:
    avail_choices = pet.get_choices()
    avail_choices_str = list_to_comma(avail_choices, conjunction='or')
    choice = raw_input(
        '\nWhat would you like to do with {}?  '
        '{}\n'.format(name, avail_choices_str))

    try:
        getattr(pet, choice)()
    except AttributeError:
        print '{} is not an available choice'.format(choice)
    except DeathException as err:
        print asciiart.death
        print err
        sys.exit(0)
    except RunAwayException as err:
        print ascciart.run_away
        print err
        sys.exit(0)