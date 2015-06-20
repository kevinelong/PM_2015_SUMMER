__author__ = 'lenny'

# attempting to program a simple receipt printer

# create the class printer
class Printer(object):
    def __init__(self):
        self.state =0

    # turn the printer on or off depending on state of toggle switch
    def toggle_switch(self):
        self.state = (self.state +1) %2

    # translate given input
    def translate_input(self, input):
        pass

    # move the print head left and right and print letters on the paper
    def move_print_head(self):
        pass

    # move the paper up and the receipt prints
    def move_paper(self):
        pass
    # paper feed function to refill paper
    def paper_feed(self):
        pass

    # turn on light to alert the user that the paper is out
    def alert_paper_out(self):
        paper_out = paper_empty
        if paper_out:
            print "paper out"


