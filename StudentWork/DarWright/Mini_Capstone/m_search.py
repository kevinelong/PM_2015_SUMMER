from Mini_Capstone.py_omdb import Search


#

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
                               "9. Quit\n"
                               ">> "))

        if choice == 1:
            title = raw_input("Enter the name of the movie:  ")
            title = title.replace(' ', '+')
            result_choice = self.full_or_common()
            self.search.set_response_details(result_choice)
            self.search.movie(title)

        elif choice == 2:
            title = raw_input("Enter the name of the TV Show:  ")
            title = title.replace(' ', '+')
            self.full_or_common()
            self.search.series(title)

        elif choice == 3:
            season = int(raw_input("Enter the number of the season: "))
            episode = int(raw_input("Enter the number of the episode:  "))
            self.full_or_common()
            self.search.episode(season, episode)

        elif choice == 9:
            exit()
    #
    # def tomatoes_choice(self):
    #     tomatoes_choice = raw_input("Do you want to see the ratings from rotten tomatoes? y/n: ").lower()
    #     if tomatoes_choice == 'y':
    #         t_choice = True
    #         self.
    #     else:
    #         t_choice = False
    #     return t_choice


    def full_or_common(self):
        """
        sets the results set
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

test = UI()
