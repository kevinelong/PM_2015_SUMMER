import time
import webbrowser

progress_report_dict = {
    'james': {'gender': "male or female", 'age': 24, 'weight': 164, 'height': 72},
    'smith': {'gender': "male or female", 'age': 24, 'weight': 164, 'height': 72},
    'gordon': {'gender': "male or female", 'age': 24, 'weight': 164, 'height': 72},
    'munster': {'gender': "male or female", 'age': 24, 'weight': 164, 'height': 72},
    'robinson': {'gender': "male or female", 'age': 24, 'weight': 164, 'height': 72}
}

def response_1():
    choice = raw_input("What would you like to know?\n"
                       "\n"
                       "1. What's my maximum heart rate for my age?\n"
                       "2. How many calories should I burn daily to reach goals?\n"
                       "3. My Progress Report.\n"
                       "4. Inspirational Quotes from Arnold\n"
                       "5. Log out.\n")
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
    else:
        return

def heart_rate():
    age = raw_input("Let's begin by finding your maximum heart rate. How old are you?")
    m_rate = 220 - int(age)  #need to fix. breaks with string
    lower_range = m_rate * 0.5
    upper_range = m_rate * 0.8
    print "You're maximum heart rate is {}\n".format(m_rate)
    time.sleep(1)
    enter = raw_input("Next we'll find our recommeded target heart rate range! Are you ready to continue?\n")
    print "Your range for you age is between {} and {}.\n" \
          "We want to stay close to being in this range to optimal burn. If you're not feeling any exertion\n"\
          "or your heart rate is too low, pick up the pace. If you're worried that you're pushing yourself\n" \
          "too hard or your heart rate is too high, back off a bit.\n" \
          "".format(lower_range,upper_range)

def my_progress():
    decision = raw_input("What would you like to do? Select 1 to view a profile or 2 to change a profile.")
    if decision == '1':
        search_report()
        my_progress()
    elif decision == '2':
        search_name = raw_input("Input the user's last name of which you'd like to review.")
        if search_name not in progress_report_dict:
            print ("The user profile you are searching for does not exist. Please make another selection.")
            my_progress()
        else:
            print "Searching for you selection, this may take a moment...\n"
            change_report(search_name)
    print "From whence we left off, here is your profile! {}".format(progress_report_dict[search_name])

def search_report():
    search_name = raw_input("Input the user's last name of which you'd like to review.")
    print "yay"
    if search_name in progress_report_dict:
        print progress_report_dict[search_name]



def change_report(name):
    change_info = raw_input("What would you like to update? Gender, Age, Weight, Height?\n")
    if change_info == 'gender':
        gender = raw_input('Please enter your updated gender: ')
        progress_report_dict[name]['gender'] = gender
    elif change_info == 'age':
        age = raw_input('Please enter your updated age (Happy Birthday!): ')
        progress_report_dict[name]['age'] = age
    elif change_info == 'weight':
        weight = raw_input('Please enter your updated weight: ')
        progress_report_dict[name]['weight'] = weight
    elif change_info == 'height':
        height  =   raw_input('Please enter your updated height: ')
        progress_report_dict[name]['height'] = height
    else:
        print "I don't understand, please make a choice from the variables given.\n"
    print "\n"
    print """
  ______                             __           _____            __        __
 /      \                           /  |         /     |          /  |      /  |
/$$$$$$  |  ______    ______    ____$$ |         $$$$$ |  ______  $$ |____  $$ |
$$ | _$$/  /      \  /      \  /    $$ |            $$ | /      \ $$      \ $$ |
$$ |/    |/$$$$$$  |/$$$$$$  |/$$$$$$$ |       __   $$ |/$$$$$$  |$$$$$$$  |$$ |
$$ |$$$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      /  |  $$ |$$ |  $$ |$$ |  $$ |$$/
$$ \__$$ |$$ \__$$ |$$ \__$$ |$$ \__$$ |      $$ \__$$ |$$ \__$$ |$$ |__$$ | __
$$    $$/ $$    $$/ $$    $$/ $$    $$ |      $$    $$/ $$    $$/ $$    $$/ /  |
 $$$$$$/   $$$$$$/   $$$$$$/   $$$$$$$/        $$$$$$/   $$$$$$/  $$$$$$$/  $$/




"""



while True:
    status = raw_input(str("How are we feeling today? Good or bad?\n")).lower()
    if status.lower() in 'good':
        print "Glad to hear it, lets get down to business!\n"
        print "You'll get the most from your workouts if you're exercising\n" \
          "at the proper exercise intensity for your health and fitness goals.\n"
        response_1()
    elif status.lower() in 'bad':
        print "Sorry to hear that, lets try to workout a way into a good time!\n"
        print "You'll get the most from your workouts if you're exercising\n" \
          "at the proper exercise intensity for your health and fitness goals.\n"
        response_1()
    else:
        print "You are either good or bad, don't try to get testy with me!"



    # input_w = raw_input(int("How much do you weight?(Round to the nearest tenth)"))


