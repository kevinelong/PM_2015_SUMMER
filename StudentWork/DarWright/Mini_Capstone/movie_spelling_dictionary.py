import enchant

# movie_dict = enchant.DictWithPWL("en_US", "movie_titles.txt")  # create dict object with PWL (text file)

class CheckSpelling(object):

    def __init__(self):
        self.movie_dict = enchant.DictWithPWL("en_US", "movie_titles.txt")  # create dict object with PWL (text file)

    def check(self, title):
        movie_suggestion = self.movie_dict.suggest(title)
        return movie_suggestion


test = CheckSpelling()
print test.check('Mad ma')
print test.check('Laska k zivotu')
