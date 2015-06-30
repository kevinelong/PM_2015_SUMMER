import time
import webbrowser

progress_report = {"gender": "male or female", "age": 24, "Weight": 164, "height": 72}

# class user_stats(object):
#     def __init__(self):
#         self.age = raw_input()
#         self.height
#         self.weight
#         self.activity_level
#         self.heartrate

    # def my_fit_questions(self):
    #     age = self.age
    #     while True:
    #         if age > 16:
    #             pass
    #         else:
#     #             print "It is recommended you be 16 years of age or older to use this program. Thank you."
#
# def heartrate():
#     age = raw_input(int("How old are you?"))
#     m_hrate = 220 - age
#     print m_hrate

def response_1():
    choice = raw_input("What would you like to know?\n"
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
        progress()
        response_1()
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


def progress():
    change_info = raw_input("What would you like to update? Gender, Age, Weight, Height?")
    if change_info not in progress_report:
        print "I don't understand, please make a choice from the variabls given."
        change_info
    else:
        for key in progress_report:
            if key == change_info:
                gender = raw_input('Please enter your updated gender: ')
                age = raw_input('Please enter your updated age(Happy Birthday!: ')
                weight = raw_input('Please enter your updated weight: ')
                height = raw_input('Please enter your updated height: ')
                print progress_report
    print "\n"
    print "                     _ _ _ _ _ _ _ _\n" \
          "                    /   _ _ _ _ _ _/\n" \
          "                   /   /\n" \
          "                  /   /\n" \
          "                 /   /\n" \
          "                /   /   _ _ _  \n" \
          "               /   /   / _   /   \n" \
          "              /   /_ _ _ /  /\n" \
          "             /_ _ _ _ _ _ _/\n"
    print "\n"
    response_1()


while True:
    status = raw_input(str("How are we feeling today? Good or bad?\n")).lower()
    if status.lower() in 'good':
        print "Glad to hear it, lets get down to business!\n"
        print "You'll get the most from your workouts if you're exercising\n" \
          "at the proper exercise intensity for your health and fitness goals.\n"
        response_1()

    else:
        print "Sorry to hear that, lets try to workout a way into a good time!\n"
        print "You'll get the most from your workouts if you're exercising\n" \
          "at the proper exercise intensity for your health and fitness goals.\n"
        response_1()



    # input_w = raw_input(int("How much do you weight?(Round to the nearest tenth)"))


