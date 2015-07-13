import enchant

class CheckSpelling(object):

    def __init__(self):
        self.movie_dict = enchant.DictWithPWL("en_US", "/Users/darwright/Python/PM_2015_SUMMER/StudentWork/DarWright/Mini_Capstone/movie_titles.txt")  # create dict object with PWL (text file)

    def check(self, title):
        movie_suggestion = self.movie_dict.suggest(title)
        return movie_suggestion


# test = CheckSpelling()
# print test.check('Mad ma')
# ['Madman', 'Madhya', 'Madame', 'Mad max', 'Za ma']
# print test.check('Laska k zivotu')
