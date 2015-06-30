# UI for omdb wrapper
from Mini_Capstone.py_omdb import Search
import sys


class UI(object):

    def __init__(self):
        self.search = Search()
        self.main_menu()

    def main_menu(self):
        print "Welcome to the movie search"
        choice = int(raw_input("Do you want to search for a:\n"
                               "1. Movie\n"
                               "2. TV Show\n"
                               "3. TV Show Episode\n"
                               "4. IMDB ID number\n"
                               "9. Quit\n"
                               ">> "))

        if choice == 1:
            title = raw_input("Enter the name of the movie:  ").decode(sys.stdin.encoding)
            title = title.replace(' ', '+')
            self.check_year()
            result_choice = self.full_or_common()
            self.plot_choice()
            self.search.set_response_details(result_choice)
            self.search.title(title)
            self.print_results()

        elif choice == 2:
            title = raw_input("Enter the name of the TV Show:  ")
            title = title.replace(' ', '+')
            result_choice = self.full_or_common()
            self.plot_choice()
            self.search.set_response_details(result_choice)
            self.search.title(title)
            self.print_results()

        elif choice == 3:
            title = raw_input("Enter the name of the TV Show: ").decode(sys.stdin.encoding)
            title = title.replace(' ', '+')
            season = self.check_season_number()
            episode = self.check_episode_number()
            result_choice = self.full_or_common()
            self.plot_choice()
            self.search.set_response_details(result_choice)
            self.search.episode(title, season, episode)
            self.print_results()

        elif choice == 4:
            imdb_id = raw_input("Enter the IMDB ID number:  ")
            result_choice = self.full_or_common()
            self.plot_choice()
            self.search.set_response_details(result_choice)
            self.search.imdbid(imdb_id)
            self.print_results()

        elif choice == 9:
            exit()

    def check_season_number(self):
        season = raw_input("Enter the number of the season: ")
        try:
            season = int(season)
        except ValueError:
            print "Not a valid number, please try again.\n"
            self.check_season_number()
        season = str(season)
        return season

    def check_episode_number(self):
        episode = raw_input("Enter the number of the episode: ")
        try:
            episode = int(episode)
        except ValueError:
            print "Not a valid number, please try again.\n"
            self.check_episode_number()
        episode = str(episode)
        return episode

    def check_year(self):
        check = raw_input("Do you know the year the movie was released? y/n> ").lower()
        if check == 'y':
            movie_year = raw_input("Please enter the year: ")
            self.search.year = '&y=' + movie_year

    def plot_choice(self):
        choice = int(raw_input("There are two options available for the Plot listing:\n"
                               "1. Full plot\n"
                               "2. Short plot\n"
                               ">> "))
        if choice == 1:
            self.search.plot = '&plot=full'

    def full_or_common(self):
        """
        sets the results set to be printed/returned
            1 = full list with tomatoes
            2 = full list without tomatoes
            3 = common list ( title, actors, plot, year)
            4 = common list with tomatoes
        """

        choice = int(raw_input("Do you want the full results, or the most common results?\n"
                               "1. Full list\n"
                               "2. Full list without Rotten Tomatoes\n"
                               "3. Common list\n"
                               "4. Common List with Rotten Tomatoes\n"
                               ">> "))
        return choice

    def print_results(self):
        if self.search.data['Response'] == "'False'":
            print u"Could not find a match for {}".format(self.search.title)
        else:
            for each in self.search.response_list:
                value = self.search.data[each]
                each = each.decode(sys.stdin.encoding)
                if each == 'Plot':
                    value = value.replace(". ", ". \n")
                    print u"{}: {}".format(each, value)
                    continue
                print u"{}: {}".format(each, value)

test = UI()
