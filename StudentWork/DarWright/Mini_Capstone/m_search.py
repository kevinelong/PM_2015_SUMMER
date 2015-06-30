from Mini_Capstone.py_omdb import Search


#

class UI(object):

    def __init__(self):
        self.search = Search()
        self.main_menu()

    def main_menu(self):
        print "Welcome to the movie search"
        choice = int(raw_input("Do you want to search for a:\n"
                               "1. Movie Title\n"
                               "2. TV Show\n"
                               "3. TV Show Episode\n"
                               "4. IMDB ID number\n"
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
            result_choice = self.full_or_common()
            self.search.set_response_details(result_choice)
            self.search.series(title)

        elif choice == 3:
            title = raw_input("Enter the name of the TV Show:  ")
            title = title.replace(' ', '+')
            season = raw_input("Enter the number of the season: ")
            episode = raw_input("Enter the number of the episode:  ")
            result_choice = self.full_or_common()
            self.search.set_response_details(result_choice)
            self.search.episode(title, season, episode)

        elif choice == 4:
            imdb_id = raw_input("Enter the IMDB ID number:  ")
            result_choice = self.full_or_common()
            self.search.set_response_details(result_choice)
            self.search.imdbid(imdb_id)

        elif choice == 9:
            exit()

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
