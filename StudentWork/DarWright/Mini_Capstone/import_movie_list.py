# coding=utf-8
"""
Write a program to read in a list/text file and grab the name of the movie in the list.
"""
import unicodedata
from django.utils.encoding import smart_str, smart_unicode

class Import(object):

    def __init__(self, input_file, output_file):
        self.title_list = []
        self.input_filename = input_file
        self.output_filename = output_file
        self.import_export()

    def import_export(self):
        filename = self.input_filename
        with open(filename) as load_import_data:
            for line in load_import_data:
                # line = unicode(line, 'utf-8')
                # line = line.encode('ascii')
                line = unicodedata.normalize('NFKD', line).encode('ascii', 'ignore')
                # line = smart_str(line)
                if '   (aka' in line:
                    continue
                else:


                    #

                    line = line[:-1]  # removes the \n from the line
                    if ' {' in line:  # removes the episode titles from list
                        new_line = line.split(' {')
                        new_line.pop()
                        line = ''.join(new_line)
                    new_line = line.split(' ')  # split the line into a list of words
                    if new_line[-1] == '(TV)':  # remove extra stuff from lines to get just the title
                        new_line.pop()
                    elif new_line[-1] == '(V)':
                        new_line.pop()
                    elif new_line[-1] == '(VG)':
                        new_line.pop()
                    new_line.pop()  # remove the year off the end
                    line = ' '.join(new_line)  # put the title back together
                    if line:  # take out the blank lines
                        self.title_list.append(line)
        self.title_list = set(self.title_list)  # remove duplicates
        self.title_list = list(self.title_list)  # put it back into a list for ease of use
        out_filename = self.output_filename
        with open(out_filename, 'w') as save_file:
            for each in self.title_list:
                save_file.write('{}\n'.format(each))

inputn = '/Users/darwright/Python/PM_2015_SUMMER/StudentWork/DarWright/Mini_Capstone/test_import2.txt'
output = '/Users/darwright/Python/PM_2015_SUMMER/StudentWork/DarWright/Mini_Capstone/test_export.txt'
# inputn = 'full_movie_list.txt'
# output = 'movie_titles.txt'
new = Import(inputn, output)
#


