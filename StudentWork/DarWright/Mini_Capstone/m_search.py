# UI for py_omdb wrapper
from Mini_Capstone.py_omdb import Search
from Mini_Capstone.movie_spelling_dictionary import CheckSpelling
import sys
import time


class UI(object):

    def __init__(self):
        self.search = Search()
        self.main_menu()
        self.movie_title = ''
        self.imdb_num = ''

    def main_menu(self):
        print "Welcome to the movie search"
        choice = raw_input("Do you want to search for a:\n"
                           "1. Movie\n"
                           "2. TV Show\n"
                           "3. TV Show Episode\n"
                           "4. IMDB ID number\n"
                           "9. Quit\n"
                           ">> ")
        choice = self.try_catch_not_an_int(choice)

        if choice == 1:
            title = raw_input("Enter the name of the movie:  ")
            self.movie_title = title
            title = self.set_title(title)
            self.get_year_input()
            result_choice = self.get_result_list_input()
            self.get_plot_choice_input()
            self.search.set_response_details(result_choice)
            self.search.title(title)
            self.print_results()

        elif choice == 2:
            title = raw_input("Enter the name of the TV Show:  ")
            self.movie_title = title
            title = self.set_title(title)
            result_choice = self.get_result_list_input()
            self.get_plot_choice_input()
            self.search.set_response_details(result_choice)
            self.search.title(title)
            self.print_results()

        elif choice == 3:
            title = raw_input("Enter the name of the TV Show: ").decode(sys.stdin.encoding)
            self.movie_title = title
            title = self.set_title(title)
            season = self.get_season_number_input()
            episode = self.get_episode_number_input()
            result_choice = self.get_result_list_input()
            self.get_plot_choice_input()
            self.search.set_response_details(result_choice)
            self.search.episode(title, season, episode)
            self.print_results()

        elif choice == 4:
            imdb_id = raw_input("Enter the IMDB ID number:  ")
            self.imdb_num = imdb_id
            result_choice = self.get_result_list_input()
            self.movie_title = 'None'
            self.get_plot_choice_input()
            self.search.set_response_details(result_choice)
            self.search.imdbid(imdb_id)
            self.print_results()

        elif choice == 9:
            exit()

    def set_title(self, title):
        title = title.decode(sys.stdin.encoding)
        title = title.replace(' ', '+')
        return title

    def get_season_number_input(self):
        season = raw_input("Enter the number of the season: ")
        try:
            season = int(season)
        except ValueError:
            print "Not a valid number, please try again.\n"
            self.get_season_number_input()
        season = str(season)
        return season

    def get_episode_number_input(self):
        episode = raw_input("Enter the number of the episode: ")
        try:
            episode = int(episode)
        except ValueError:
            print "Not a valid number, please try again.\n"
            self.get_episode_number_input()
        episode = str(episode)
        return episode

    def get_year_input(self):
        check = raw_input("Do you know the year the movie was released? y/n> ").lower()
        if check == 'y':
            movie_year = raw_input("Please enter the year: ")
            self.search.year = '&y=' + movie_year

    def get_plot_choice_input(self):
        choice = raw_input("There are two options available for the Plot listing:\n"
                           "1. Full plot\n"
                           "2. Short plot\n"
                           ">> ")
        choice = self.try_catch_not_an_int(choice)

        if choice == 1:
            self.search.plot = '&plot=full'

    def get_result_list_input(self):
        """
        sets the results set to be printed/returned
            1 = full list with tomatoes
            2 = full list without tomatoes
            3 = common list ( title, actors, plot, year)
            4 = common list with tomatoes
        """

        choice = raw_input("Do you want the full results, or the most common results?\n"
                           "1. Full list\n"
                           "2. Full list without Rotten Tomatoes\n"
                           "3. Common list\n"
                           "4. Common List with Rotten Tomatoes\n"
                           ">> ")
        choice = self.try_catch_not_an_int(choice)
        return choice

    def print_results(self):

        if self.search.data['Response'] == 'False':
            if self.movie_title == 'None':
                print u"Could not find a match for IMDB # {}".format(self.imdb_num)
            else:
                check_spelling = CheckSpelling()
                suggestions = check_spelling.check(self.movie_title)
                print u"Could not find a match for {}".format(self.movie_title)
                print "Possible suggestions: "
                for each in suggestions:
                    print each + "   "
            time.sleep(5)
            self.main_menu()
        else:
            for each in self.search.response_list:
                value = self.search.data[each]
                each = each.decode(sys.stdin.encoding)
                if each == 'Plot':
                    value = value.replace(". ", ". \n")
                    print u"{}: {}".format(each, value)
                    continue
                print u"{}: {}".format(each, value)
        self.reset()

    def reset(self):
        """
        reset the data/clear out the data so more than one search can happen
        :return:
        """
        self.search = Search()
        self.movie_title = ''
        self.imdb_num = ''
        time.sleep(3)
        self.main_menu()

    def try_catch_not_an_int(self, choice):
        try:
            choice = int(choice)
        except ValueError:
            print "Please enter a number only."
            self.reset()
        return choice


test = UI()
