__author__ = 'darwright'
"""
Write a program to read in a list/text file and grab the name of the movie in the list. List from imdb
"""
import re
class Import(object):

    def __init__(self):
        self.title_list = []

    def open_file(self):
        filename = 'test_import.list'


        with open(filename) as load_import_data:
            for line in load_import_data:
                if '   (aka' in line:
                    # line = ''
                    continue
                else:
                    print line
                    line = line[:-1]
                    # match = re.findall(r'(\d{4})', line)
                    # match = str(match)
                    # print match
                    # line.replace('(' + match + ')', '')
                    # print match
                    # print line
                    # line = line[:-7]
                    # year = [int(s) for s in line.split() if s.isdigit()]
                    # print year
                    new_line = line.split(' ')
                    print new_line
                    new_line.pop()
                    print new_line
                    line = ' '.join(new_line)
                    print line
                    self.title_list.append(line)
        for item in self.title_list:
            if item == '':
                self.title_list.remove(item)

        # print self.title_list

new = Import()
new.open_file()

# '   (aka Pferdediebe am Missouri (1952))	(Austria)