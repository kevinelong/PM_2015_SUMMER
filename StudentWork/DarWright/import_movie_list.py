__author__ = 'darwright'
"""
Write a program to read in a list/text file and grab the name of the movie in the list. List from imdb
"""
class Import(object, input_file, output_file):

    def __init__(self):
        self.title_list = []
        self.input_filename = ''
        self.output_filename = ''

    def open_file(self):
        filename = self.input_filename
        with open(filename) as load_import_data:
            for line in load_import_data:
                if '   (aka' in line:
                    continue
                else:
                    line = line[:-1]  # removes the \n from the line
                    new_line = line.split(' ')  # split the line into a list of words
                    new_line.pop()  # remove the year off the end
                    line = ' '.join(new_line)  # put the title back together
                    self.title_list.append(line)
        for item in self.title_list:
            if item == '':
                self.title_list.remove(item)

        out_filename = self.output_filename = ''
        with open(out_filename, 'a') as save_file:
            for each in self.title_list:
                save_file.write('{}\n'.format(each))
inputn = 'full_movie_list.txt'
output = 'movie_titles.txt'
new = Import(inputn, output)


