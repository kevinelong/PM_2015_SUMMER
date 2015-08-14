import time
import webbrowser
import cPickle as pickle

username = "mattija"
userpassword = 124578985

#**************************************************************************************#
#                         File path information                                        #
#                         Progress report dictionary                                   #
#**************************************************************************************#


pickle_file = '/home/jay/PycharmProjects/PM_2015_SUMMER/StudentWork/JayMattingly/PMSchoolWork/test.pickle'


progress_report_dict = [
    {'fname': 'james', 'gender': "gender", 'age': 24, 'weight': 164, 'height': 72}
]

#****************************************************************************************#
#                           Used to save progress report,                                #
#                           opens file to regain progress                                #
#                           made to client reports                                       #
#                                                                                        #
#****************************************************************************************#

def write_to_file(progress_report_dict):            #saves entries to file
    with open(pickle_file, 'w') as prd_file:
        pickle.dump(progress_report_dict, prd_file)

def get_from_file():                                #retrieves file to be continued
    with open(pickle_file) as prd_file:
        loaded_obj = pickle.load(prd_file)
    return loaded_obj

def search_report():
    search_name = raw_input("Input the user's first name of which you'd like to review.")
    for i in progress_report_dict:
        if search_name == i["fname"]:
            print 'name: {}\n' \
                  'gender: {}\n' \
                  'age: {}\n' \
                  'weight: {}\n' \
                  'height: {}'.format(i['fname'],i['gender'],i['age'],i['weight'],i['height'])


#****************************************************************************************#
#                           Functions that run the program                               #
#                           heart rate, progress report,                                 #
#                           changing report, writing to                                  #
#                           report(add profiles)                                         #
#****************************************************************************************#

def heart_rate():
    age = raw_input("Input age of individual\n"
                    ":")
    age = try_catch_int(age)        #catches if input i
    m_rate = 220 - age  #need to fix. breaks with string
    lower_range = m_rate * 0.5
    upper_range = m_rate * 0.8
    print "Maximum heart rate is {}\n".format(m_rate)
    enter = raw_input('Press enter to continue to target heart range.')
    time.sleep(1)
    print "Your range for you age is between {} and {}.\n" \
          "We want to stay close to being in this range to optimal burn. If you're not feeling any exertion\n"\
          "or your heart rate is too low, pick up the pace. If you're worried that you're pushing yourself\n" \
          "too hard or your heart rate is too high, back off a bit.\n" \
          "".format(lower_range,upper_range)
    time.sleep(10)
    return

def add_client_profile():
    fname = raw_input("Enter your client's first name\n"
                      ":")
    # lname = raw_input("Enter your client's last name\n"
    #                   ":")
    gender = raw_input("M. Male\n"
                       "F. Female\n"
                       ":")
    age = raw_input("Birth year?\n"
                    ":")
    weight = raw_input("Weight(lbs)?\n"
                       ":")
    height = raw_input("Height(centimeters)?\n"
                       ":")
    contact_entry = {"fname": fname, "gender": gender, "age": age, "weight": weight, "height": height}

    choice = str.lower(raw_input("Would you like to add this contact? Yes or No?\n"
                       ""))
    if choice == 'yes' or 'y':
        progress_report_dict.append(contact_entry)
        request = raw_input("Contact added successfully!\n" \
              "Would you like to add another contact?\n" \
              "Y or N?\n" \
              ":").lower()
        if request == 'y':
            add_client_profile()
        else:
            my_progress()
    else:
        print "Add contact cancelled!"
        time.sleep(2)
        my_progress()



def my_progress():
    decision = raw_input("What would you like to do?\n"
                         "A. Add new client profile\n"
                         "P. View a profile\n"
                         "C. Change a profile\n"
                         "X. Return to Main Menu\n"
                         "V. See all profile data\n"
                         "\n"
                         ":").lower()
    if decision == 'p':
        search_report()
        my_progress()
    elif decision == 'c':
        search_name = raw_input("Input the user's last name of which you'd like to review.")
        if search_name not in progress_report_dict:
            print ("The user profile you are searching for does not exist. Please make another selection.")
            my_progress()
        else:
            print "Searching for your selection, this may take a moment...\n"
            change_report(search_name)
            print "{}'s profile {}".format(search_name,progress_report_dict[search_name])
    elif decision == 'x':
        response_1()
    elif decision == 'v':
        print get_from_file()
        my_progress()
    elif decision == 'a':
        add_client_profile()
        my_progress()

    else:
        print "\n"
        time.sleep(0.5)
        print "That is an invalid entry, please re-enter your selection."
        print "\n"
        time.sleep(0.5)
        my_progress()


def change_report(name):
    change_info = raw_input("What would you like to update?\n"
                            "1.Gender\n"
                            "2.Age\n"
                            "3.Weight\n"
                            "4.Height\n"
                            "5.Save data\n"
                            "6.Exit\n"
                            ":")
    if change_info == '1':
        gender = raw_input('Please enter your updated gender: ')
        progress_report_dict[name]['gender'] = gender
        change_report(name)
    elif change_info == '2':
        age = raw_input('Please enter your updated age (Happy Birthday!): ')
        progress_report_dict[name]['age'] = age
        change_report(name)
    elif change_info == '3':
        weight = raw_input('Please enter your updated weight: ')
        progress_report_dict[name]['weight'] = weight
        change_report(name)
    elif change_info == '4':
        height = raw_input('Please enter your updated height: ')
        progress_report_dict[name]['height'] = height
        change_report(name)
    elif change_info == '5':
        write_to_file(progress_report_dict)
        change_report(name)
    elif change_info == '6':
        response_1()
    else:
        print "That is an invalid entry, please re-enter your selection.\n"
        change_report(name)

def try_catch_int(num):
    try:
        num = int(num)
    except ValueError:
        print "You must enter your age in numeric characters!"
    return num

#****************************************************************************************#
#                                   User Interface                                       #
#                                   Gives choices                                        #
#                                   Opens webpage                                        #
#                                                                                        #
#****************************************************************************************#

def response_1():
    choice = raw_input("Please select from the choices given.\n"
                       "\n"
                       "1. Heart Rate Guide\n"
                       "2. Calorie calculator\n"
                       "3. Client Progress Report\n"
                       "4. My schedule\n"
                       "5. Log out.\n"
                       ":")
    if choice == '1':
        heart_rate()
        response_1()
    elif choice == '2':
        time.sleep(1)
        print "You're now being redirected to 'freedieting.com' if you do not see the page, please wait."
        time.sleep(1)
        webbrowser.open('http://www.freedieting.com/tools/calorie_calculator.htm')
        response_1()
    elif choice == '3':
        my_progress()
    elif choice == '4':
        pass
    elif choice == '5':
        return
    else:
        print "That is an invalid entry, please re-enter your selection."
        response_1()


# def app_starter():
#     print "Please enter you credentials here."
#     userinputname = raw_input("Username\n"
#                               ":")
#     userinputpass = int(raw_input("Password\n"
#                               ":"))
    # if (userinputname, userinputpass) == (username, userpassword):
while True:
    print """

                Welcome to my little fitness helper!
                Where you can track all your clients
                    in one handy little app!


                copyright javiair.mattingly.llc
        """
    status = raw_input(str("Input F to continue.\n"
                           "Input C to view element\n"
                           "Input E to close application\n"
                           "\n"
                           ":")).lower()
    if status.lower() in 'f':
        response_1()
    elif status.lower() in 'c':
        webbrowser.open('https://github.com/kevinelong/PM_2015_SUMMER/blob/master/StudentWork/JayMattingly/Midcap/Midcapproject.py')
    elif status.lower() in "e":
        print "Saving application data...\n" \
              "Done!\n" \
              "Good bye!"
        exit()
    else:
        print "That is an invalid entry, please re-enter your selection."
        time.sleep(2)
else:
    print "You're username or password is invalid. Please try again."
    time.sleep(1)
# app_starter()

# app_starter()

