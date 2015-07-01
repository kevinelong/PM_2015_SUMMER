__author__ = 'darwright'
import enchant
# i want to eb able to recommend spelling checks and movie title/year options for movie searches
#
# d = enchant.Dict("en_US")   # create dictionary for US English
# # print d.check("enchant")
# # print d.check("enchnt")
# #
# # print d.suggest("enchnt")
# # ['enchant', 'enchants', 'enchanter', 'penchant', 'incant', 'enchain', 'enchanted']
#
# print d.suggest('This is a relly long sentnece wil it work?')  # no
#
# print d.suggest("Hw many wrds")  # fail
#
# print d.suggest("A ghst")  # best to check each word individually
#
#
# d.add()

# pwl = enchant.request_pwl_dict("test_list.txt")  # set Personal Word List
movie_dict = enchant.DictWithPWL("en_US","test_list.txt")  # create dict object with PWL (text file)
print movie_dict.suggest('Last Plan Out')