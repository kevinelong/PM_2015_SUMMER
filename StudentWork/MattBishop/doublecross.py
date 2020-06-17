from sys import exit
# To be implemented through a scenario challenge
import random
import time

# What you begin the game with
inventory = ['quarter', 'dime', 'nickel']
# This list will be a part of the check against being framed and losing the game
clues = []
# This list will be a part of the 'check_lose' function, one of two ways of losing the game
evidence_planted = []

# Adds helpful objects throughout story; some will be conditional to gaining clues
def add_to_inventory(item):
    inventory.append(item)
# You can lose items in various ways; a resulting loss may prevent access to clues
def remove_inventory_item(item):
    inventory.remove(item)
# A function to add clues throughout investigation
def clues_found(item):
    clues.append(item)
    print "These are your clues: {}.".format(clues)

# The function that will be called each time the program plants evidence against the player
def framed(item):
    evidence_planted.append(item)

# You can remove planted evidence with successful attribute checks
def dispose_frame(item):
    evidence_planted.remove(item)

# If your character makes a wrong decision without the appropriate attributes, they can be killed
def death():
    print "Looks like this is the end of the road. Thanks for playing!"
    exit(1)

# A late game, periodic check to see if the computer has planted compelling evidence to warrant a loss
def check_lose():
    if evidence_planted > clues:  # This is probably not going to work; will fix when I finish text!
        print """
*text*
"""
    lose()

# And another way to lose (through encounters)
def lose():
    print """
Looks like you were outsmarted this time, ace. You'll have loads of time to consider all of your mistakes in the can.
"""
    print "Thanks for playing!"
    exit(1)

# This occurs at the end scene
def win():
    print """
*text*
"""
    print "Thanks for playing!"
    exit(1)


print """
____________________________________________________________________________________________________________________________________________________________________________________________
8 888888888o.          ,o888888o.     8 8888      88 8 888888888o   8 8888         8 8888888888                 ,o888888o.    8 888888888o.      ,o888888o.       d888888o.      d888888o.
8 8888    `^888.    . 8888     `88.   8 8888      88 8 8888    `88. 8 8888         8 8888                      8888     `88.  8 8888    `88.  . 8888     `88.   .`8888:' `88.  .`8888:' `88.
8 8888        `88. ,8 8888       `8b  8 8888      88 8 8888     `88 8 8888         8 8888                   ,8 8888       `8. 8 8888     `88 ,8 8888       `8b  8.`8888.   Y8  8.`8888.   Y8
8 8888         `88 88 8888        `8b 8 8888      88 8 8888     ,88 8 8888         8 8888                   88 8888           8 8888     ,88 88 8888        `8b `8.`8888.      `8.`8888.
8 8888          88 88 8888         88 8 8888      88 8 8888.   ,88' 8 8888         8 888888888888           88 8888           8 8888.   ,88' 88 8888         88  `8.`8888.      `8.`8888.
8 8888          88 88 8888         88 8 8888      88 8 8888888888   8 8888         8 8888                   88 8888           8 888888888P'  88 8888         88   `8.`8888.      `8.`8888.
8 8888         ,88 88 8888        ,8P 8 8888      88 8 8888    `88. 8 8888         8 8888                   88 8888           8 8888`8b      88 8888        ,8P    `8.`8888.      `8.`8888.
8 8888        ,88' `8 8888       ,8P  ` 8888     ,8P 8 8888      88 8 8888         8 8888                   `8 8888       .8' 8 8888 `8b.    `8 8888       ,8P 8b   `8.`8888. 8b   `8.`8888.
8 8888    ,o88P'    ` 8888     ,88'     8888   ,d8P  8 8888    ,88' 8 8888         8 8888                      8888     ,88'  8 8888   `8b.   ` 8888     ,88'  `8b.  ;8.`8888 `8b.  ;8.`8888
8 888888888P'          `8888888P'        `Y88888P'   8 888888888P   8 888888888888 8 888888888888               `8888888P'    8 8888     `88.    `8888888P'     `Y8888P ,88P'  `Y8888P ,88P'
_____________________________________________________________________________________________________________________________________________________________________________________________

  ,---.        ,--.                    ,--.         ,--.                          ,--.               ,--.                          ,--.
 /  O  \     ,-'  '-. ,---.,--.  ,--.,-'  '-.,-----.|  |-. ,--,--. ,---. ,---.  ,-|  |     ,--,--. ,-|  |,--.  ,--.,---. ,--,--, ,-'  '-.,--.,--.,--.--. ,---.      ,---.  ,--,--.,--,--,--.,---.
|  .-.  |    '-.  .-'| .-. :\  `'  / '-.  .-''-----'| .-. ' ,-.  |(  .-'| .-. :' .-. |    ' ,-.  |' .-. | \  `'  /| .-. :|      \'-.  .-'|  ||  ||  .--'| .-. :    | .-. |' ,-.  ||        | .-. :
|  | |  |      |  |  \   --./  /.  \   |  |         | `-' \ '-'  |.-'  `)   --.\ `-' |    \ '-'  |\ `-' |  \    / \   --.|  ||  |  |  |  '  ''  '|  |   \   --.    ' '-' '\ '-'  ||  |  |  \   --.
`--' `--'      `--'   `----'--'  '--'  `--'          `---' `--`--'`----' `----' `---'      `--`--' `---'    `--'   `----'`--''--'  `--'   `----' `--'    `----'    .`-  /  `--`--'`--`--`--'`----'
                                                                                                                                                                   `---'
"""
time.sleep(3)
print """
Welcome to Double Cross, a text based detective story. Let's begin by creating a character.
"""

# the name is self explanatory - the function that is called to specify and add points to each attribute
def add_character_points():
    attribute = raw_input("\nWhich attribute? Strength, Agility, Perception, Intuition, or Luck?\n").lower()

    if attribute in my_character.keys():
        amount = int(raw_input("By how much?  "))

        if (amount > my_character['points']) or (amount <= 0):
            print "Not enough points!"
        else:
            my_character[attribute] += amount
            my_character['points'] -= amount
    else:
        print "\nThat attribute doesn't exist!\n"


# to see a list of assigned attributes, remaining points
def print_character():
    for attribute in my_character.keys():
        print attribute, " : ", my_character[attribute]


my_character = {'name': '', 'strength': 10, 'agility': 10, 'perception': 10, 'intuition': 10, 'luck': 10, 'health': 100,
                'points': 50}

running = True  # Will continue character creation until state is changed

my_character['name'] = raw_input("What is your character's name? ")

print """
Let's assign points to your character. Each attribute will affect game play in different ways, such as
displaying special options during scenes, which will aid you in solving mysteries, identifying clues and
character interaction.
"""
raw_input('Press Enter to continue...')

print """
Below is a description of each attribute:

Strength = How strong you are. This attribute primarily governs hitting others, intimidation, etc.
Agility = How quick you are. This attribute primarily governs avoiding danger, being quick to the draw, etc.
Perception = How easily you see what others don't. This attribute is most useful during investigations.
Intuition = How empathetic you are. This attribute is most useful during investigations.
Luck = Pure, dumb luck. A high luck gives you advantages other characters wouldn't normally have!
"""

while running:
    print "\nYou have", my_character['points'], "points left.\n"
    print "1. Add points\n2. See current attributes\n3. Go to game when finished assigning points.\n"

    choice = raw_input("Choice:  ")

    if choice == "1":
        add_character_points()
    elif choice == "2":
        print_character()
    elif choice == "3":
        running = False  # Stops the character creation and goes into Scenes
    else:
        pass

# An empty class. The initial idea was to have each child of Scene inherit all actions from the parent, but that design
# choice turned out to be a poor decision. It was far too static and I needed more dynamic functions to change
# conditions. However, since the game engine is essentially built around the finite state of these classes (another
# regretful design choice) I decided to leave the parent to avoid creating a new engine - time constraints were the most
# pressing issue in the decision. Lesson learned!
class Scene(object):
    def __init__(self):
        pass


# Essentially the game revolves around numerous nested conditions to advance game play, the manipulation of lists that
# ultimately determine whether the player wins or loses and the implementation of simple yet well-suited functions. I
# really only use a class once, which is to define a 'game map', or list of child classes of Scene. That variable is
# then called with the 'play' function.
class Office(Scene):
    def enter(self):
        return 'office_building'

    print """
The year is 1944 and you live in the greatest city on Earth - Chicago. You've managed to avoid the draft (for now) and
have been scrapping by for years as a private investigator. The pre-war years were a goldmine, filled with jilted
lovers, insurance and corporate fraud, all manner of scams and schemes and the occasional police contract. And even
though business has steadily declined since the world went to hell, you've always managed to get by. This time, though,
is different. You're on your last dime and haven't had a real case in two months. The water was shut off yesterday, the
lights are about to go out and the landlord will be coming down on you any day now. You've always heard stories about
the Cook County Almshouse - it looks like you'll be getting a firsthand tour real soon.
"""
    raw_input("Press Enter to continue...  ")

    print """
That's why the knock on the door is surprising but welcome, like Christmas come early. You open the door and are greeted
with a confident and cool woman, maybe in her late forties. She is smartly dressed in a freshly pressed dress and a
button up, waist-cinching jacket.  Her dark hair is pulled up in a tight bun nested beneath a glamorous pillbox hat. She
looks you up and down, regarding your disheveled state and says dryly, "Are you going to let me in or should I make an
appointment - seeing as how you are obviously a very busy individual." Normally you would not be inclined to entertain
such behavior, but a customer is a customer and your confidence is as threadbare as your cheap suit. You mumble a
greeting and open the door wide. The woman breezes right past you and looks intently around your office.
"""


def dialogue_tree():
    tree_input = raw_input("""
What's your next move, ace?

A.) "Say there - you wanna drink?"
B.) "What can I do for you, Miss uh..."
C.) "Why don't you have a seat and tell me what brings you to my office today."
""").lower()

    if tree_input == 'a':
        print """
"I suppose. What do you have?"

You open the drawer to your woefully stocked liquor cabinet and produce a second-rate bottle of scotch whiskey.

"And I suppose that will have to do," she says with a sigh. She eyes the bottle warily but accepts the glass readily,
seemingly grateful.
"""
        if my_character['intuition'] >= 30:
            print """
Your high Intuition has given you an unexpected insight: As she takes a pull from the glass, you notice that her hands
shake. You stare for another half second - despite her outward appearance she doesn't seem as well-collected as you
previously believed.

"Look, I deal with all sorts of cases and have seen just about everything under the sun. There's no need to be
nervous."

She glares at you and her demeanor shifts from cool to frosty. The nervousness immediately vanishes; the mask of control
that had momentarily slipped off is now back on, firmly in place.

"I am certainly not nervous. I am here because I have need of your services. Will you assist me or not?"

"Of course. Of course I will." Your slow nod seems to reassure her a bit but you already get the suspicion
that your new client is already up to no good.
"""
        dialogue_tree()

    elif tree_input == 'b' or tree_input == 'c':
        print """
"My name is Martha Sternwood. I represent the interests of my late husband, Earl Sternwood, an executive accountant with
U.S. Steel. He was murdered and robbed last night, his body left in an alley off West Lexington Street in Lawndale."

Your ears perk up like a mut being called in for supper. If Mrs. Sternwood's recently departed spouse actually brushed
elbows with the types you've seen at all those fancy restaurants and clubs in the Loop, than she may think your time is
worth more than it actually is.

"Lawndale, huh? That's an awful dangerous neighborhood for a glorified bookkeeper to be traipsing around in."
"""
        raw_input("Press Enter to continue...  ")
        print """
"Executive accountant, detective. He was head of accounts receivable for one of the largest corporations in the world.
He handled hundreds of thousands of dollars in invoices every day, from all across the world. He was an important man
in an important company... and I believe his murder wasn't a simple mugging."

Her words hang in the air for a bit, the suspicion in her voice as palpable as the burn of the cheap scotch down a dry
throat.

"Any particular reason why you don't think the cops are doing their job, Mrs. Sternwood? Or even U.S. Steel, for that
matter - hell, I'm willing to bet that they have a small army of guys like me on retainer, just waiting for the chance
to make a name for themselves."

"No doubt, detective. Let's just say I suspect that Mr. Sternwood stumbled across an account that he shouldn't have. The
weekend before he died, he confided in me that he found a dummy account that was receiving vast sums of money from
illegal loans. He told me he wanted to go to the police but suspected he was being followed. He wouldn't tell me who he
thought was following him. I didn't doubt what he said about the account but, I admit, I thought that he was being
paranoid about being stalked. When I received the call that Earl..."

She tears up a bit, shakes her head and downs the last of the scotch in her glass.
"""
        raw_input("Press Enter to continue...  ")

        print """
"When the police called, Earl had been dead several hours. His wallet, money - everything had been taken. The only
reason they identified him as quickly as they did is because a coworker of his happened to be passing by. A coworker who
had just happened to walk down a dark alley, pass through police tape and pulled aside an officer to tell them who they
had. And, oddly enough, not only did the police not question the man, they immediately labeled the case a mugging gone
wrong and rushed the body to the morgue."

"I see. So you think that maybe someone at U.S. Steel had something to do with this? Someone who didn't want the
information your husband had out in the open? That doesn't explain the police's reaction to the crime though, nor why
your husband was where he was found."

"I'm not presuming anything," Mrs. Sternwood says as she eyes you levelly. "That's your job, detective. I want you to
find my husband's killer and bring that person to justice. I am willing to pay you one thousand dollars for your
efforts."

The case sounded a lot like chasing ghosts - there were no leads, no evidence you've seen or heard of yet, and
apparently no witnesses. Just the hollow suspicions of a grieving widow, held together by the paranoia of her late
husband. But one thousand dollars... that would keep you set for the better part of a year and was a hell of a sight
better than the change that rattled in your pocket.

"Sounds tricky," you say as you cross behind your desk. "I'll need an advance. To cover expenses, of course."
"""
        raw_input("Press Enter to continue...  ")
        print """
"Will one hundred dollars do?"

She doesn't hesitate for a moment - she produces a few bills and hands them to you.

"I assume this means you accept my case, detective?"

"Yeah, I guess it does." You pocket the money, raise your glass to Mrs. Sternwood, and down the scotch. That cheap
scotch of yours has never tasted quite as good as it does now.

"Excellent. Here is the address of the crime scene - I expect you go there promptly."

She turns to leave, stops short of the door and turns around to face you.

"And detective... I hope you understand that I expect results. Do not underestimate my resolve in finding the person who
did this to Earl and me. You will find the man who murdered my husband. I'll be in touch soon to check on your
progress."

With those parting words, she whisks right out the door, just as quickly as she entered your life.

One thousand dollars... you'd gladly have done much more than solve some second-rate mystery for that kind of dough.
There's no time to waste - you slip on your coat and head out the door.
"""

        add_to_inventory('$50 dollar bill')
        add_to_inventory('$20 dollar bill')
        add_to_inventory('$5 dollar bill')
        print "You now have {}.".format(inventory)
    else:
        print "Please enter the letter that corresponds with the dialogue you wish to choose."
        dialogue_tree()


dialogue_tree()

raw_input("""
Press Enter to continue...  """)


class OfficeBuilding(Scene):
    def enter(self):
        return 'city_street'

    print """
You step into the hallway of your building and heads toward the stairwell. The place seems more a dump than usual -
your heels click on the scuffed and dirty concrete floors. The plaster on the ceiling has long ago swelled and cracked,
leaving deep fissures that occasionally rain down lime and cement. More than one standing ashtray has overflown with the
burnt ends of cigarettes, leaving behind the stale stench of cheap tobacco. The building is a hold over from another
time, an easy target for the wrecking ball and the inexorable march of progress; in short, a dinosaur.

Many of the offices you pass have long since been abandoned, but you can't decide if the tenets moved on to greener
pastures or simply went bust. Occasionally a new sucker would arrive, a shifty salesman to peddle one scam or another,
only to leave behind an abandoned room full of empty dreams just a scant few weeks later.

Frankly, it's a wonder you get any business at at all - only the foolish still seem to tread here.
"""


raw_input("""
Press Enter to continue...  """)

print """
As you make your way to the first floor and close to the entrance, you slow down to gingerly pass outside the door of
the building super, Joey Malone. If a weasel could stand on it's hind legs and walk and talk like a two-bit hustler than
there would be a picture of Joey's face in some scientific journal. You're almost positive Joey feels the same way about
you, but at least you can account for some measure of personal hygiene.

You are almost on your tiptoes when the door slams open and Joey pierces you with a withering gaze.

"So, ace, where'ya off to? Gonna crack a big case or something?" Joey flashes a cruel smile; his stained teeth spread
across his face, all black and yellow.

"As a matter of face, yes I am." You attempt to brush past Joey but he puts a grimy hand on your chest and pushes you
back a bit.

"Hold on there, ace. You and me have got some business to settle. I've been asking for a week now - where's the rent
at... " He licks his cracked lips and sneers. "... detective?"
"""


def dialogue_tree():
    tree_input = raw_input("""
What's your next move, ace?

A.) "Sorry, Joey - I still don't have it yet."
B.) Pay Joey with half of your advance.
C.) "Why don't you go get stuffed, you rotten snake."
""").lower()
    if tree_input == 'a':
        print """
"You know how hard it is out there to turn a dime," you say to Joey. "I just need a bit more time to get some scratch
together and have another go at it, that's all."

Joey seems unmoved by your financial shortcomings.

"Now listen here, you little punk. You better have something to give me or I'll throw you out on your ass in two seconds
flat, understand?"
"""
        if my_character['strength'] >= 40:
            print """
Your exceptional Strength gives you an advantage in this situation: You step right up to Joey's face, stare him down and
say "No, I don't believe you will." You can see his beady little eyes darting back and forth, weighing the
possibilities, the fear reeking from his every pore. It is obvious to both of you that Joey certainly cannot back up his
claim.

"Look... there's no need for either of us to get strong." Joey takes a step back, stopping short of the wall. "But the
fact remains you still owe me rent!"
"""
        dialogue_tree()

    elif tree_input == 'b':
        print """
You produce one of your fifty dollar bills and hand it to the little rat. He snatches it away quickly, examines it
carefully and says, "Well... looks like you have been holding out on me, slick. Where'd you get this then?"

"Like I said, I got a case. A good one. I thought that maybe you'd be happy for me, Joey."

"That's Mr. Malone to you, wise guy." He stares at you for a moment and you can almost see the hamster slowly turning
that creaky wheel inside his big, dumb skull. "I don't suppose this has anything to do with that dame that cam breezing
in her a while ago, does it?"

"Dame? What dame? I didn't see no dame."

"Huh." Joey looks down, sucks his teeth and turns back to his office. "Hey, ace," Joey calls over his shoulder. "Don't
be late on the rent again, understand?" He closes the door to quite forcefully; a trail of white dust billows out from
the ceiling.

You understand, all right. You understand that just as soon as you break this case, you're gonna give that little
twit more than just his rent. You swing open the front entrance doors and step out into the city.
"""
        remove_inventory_item('$50 dollar bill')
        print "You now have {}.".format(inventory)

    elif tree_input == 'c':
        print """
"What did you say?! Joey lets out a low roar. Apparently, he doesn't like to be spoken to in such a way...
"""
        if my_character['strength'] >= 30:
            print """
Your exceptional Strength can give you an advantage in this situation. You are more than certain that hitting the little
slug in his face will change his tune.
"""
            choice = raw_input("Do you wish to use this attribute to your advantage? Enter Yes or No.  ").lower()
            if choice == 'yes':
                print """
It was easier than breathing - you catch Joey by surprise with a quick jab right across the chin. He falls quickly, like
a sack of potatoes. He rolls around for a moment, disoriented and then looks at you, terrified.

"What are you, off your rocker or something?!"

"No, Joey. I'm not. Just tired of having my chops busted by a fat-head like you. Now why don't you crawl back in your
 office and forget this every happened. Understand?"

Joey nods his head vigorously and practically leaps back into the office. You wonder briefly if Joey has any friends
that you should be worried about, but the thought seems ridiculous. He had what was, to your mind, a long time coming to
him. You swing open the front entrance doors and step out into the city.
"""
            elif choice == 'no':
                print """
You decide that restraint is the better part of valor... or some other such nonsense.

"Easy, Joey - I'm sorry. It's been a rough week."

"Why don't you just cough over the dough, tough guy?"
"""
                dialogue_tree()
            else:
                print "Please enter yes or no to make a selection."
                dialogue_tree()

        elif my_character['strength'] < 40:
            print """
... and maybe it's not entirely in your best interest to upset him. He seems a bit... unstable.
"""
            dialogue_tree()

    else:
        print "Please enter the letter that corresponds with the dialogue you wish to choose."
        dialogue_tree()


dialogue_tree()

raw_input("""
Press Enter to continue...  """"")


class CityStreet(Scene):
    def enter(self):
        return 'crime_scene'

    print """
The air is electric as you exit that tomb of an office building and out into the city streets. It's quiet out - you
watch a few people dart to and fro, busy with life's little errands. Otherwise the street is rather empty. Good; just
the way you like it.

A feculent, old drifter spies you exiting the building and approaches. He reeks of a week long drinking binge,
punctuated by bouts of vomiting, unconsciousness and late nights in gutters.

"Say, mack - spare a dime for a drink?"
"""


def dialogue_tree():
    tree_input = raw_input("""
    What's your next move, ace?

    A.) Give the poor sap a dime.
    B.) You're feeling generous - give the man a quarter.
    C.) "Get the hell out of my way, creep."
""").lower()

    if tree_input == 'a':
        print """
"Thanks a lot, mister."

The man quickly pockets the coin and begins to amble off. You wonder which gutter he'll end up in tonight. Poor
bastard - just another hard case in a city full of hard cases. But who can blame him? No one seemed to know what they
were doing, what direction they were headed. And no one had any answers - not the president, not the churches, not the
police. The only piece of advice they could offer was the same old, tired dance an endless line of buffoons from the
beginning of time have repeated; look for the light at the end of the tunnel. Good times were coming!

The only good time coming for your new friend was that first sip of booze, the head rush of feeding an insatiable beast.
It was all down hill from there.

You shake your head - you've got bigger fish to fry and a crime scene to get to. You make your way down to the bus
station, your pockets a little lighter.
"""

        remove_inventory_item('dime')
        print "You now have {}.".format(inventory)

    elif tree_input == 'b':
        print """
"Really?! Thanks a lot, mister!"
"""
        remove_inventory_item('quarter')
        print "You now have {}.".format(inventory)

        if my_character['perception'] >= 30:
            print """
Your high Perception gives you an unexpected insight: You remember seeing this fellow coming in this morning, sprawled
along the sidewalk.

"Suppose you've been out here for a while, haven't you? Trying to scrounge up enough scratch for a whiskey?"

"You better believe it. It ain't easy, you know."

"Oh, I have no doubt. Say, let me ask you a question..."

You describe Mrs. Sternwood to the man. He listens patiently, nodding his head.

"Oh yeah, I seen her. Strange bird, that one. She must'a walked around the block four times before she went inside
that building." He nods toward your office building.

"Any idea what she was up to?" You hand the man a cigarette and light it for him. If he wasn't willing to talk before,
he certainly is now. He takes a deep drag, exhales the smoke and grins.

"If I didn't know any better, I'd say she was casing the joint!"

"What's that supposed to mean?"

"Listen, I don't know nothing. But if I were you and happened to be mixed up in some business with her... let's just say
if might not be a bad idea to watch your back." He gives you another broad grin and saunters off like a millionaire on a
stroll through Central Park; a cigarette in one hand and all the money he'll ever need in the world in the other.

You can't help but watch him as he leaves - it's amazing when the world can still throw surprises at you.

Time to go to work. You walk down to the bus station, on your way to a (most likely) cold crime scene.
"""

        elif my_character['perception'] < 30:
            print """
You watch as the man slinks off, back into the shadows of the buildings. You wonder which gutter he'll end up in
tonight. Poor bastard - just another hard case in a city full of hard cases. But who can blame him? No one seemed to
know what they were doing, what direction they were headed. And no one had any answers - not the president, not the
churches, not the police. The only piece of advice they could offer was the same old, tired dance an endless line of
buffons from the beginning of time would repeat; look for the light at the end of the tunnel. Good times were coming!

The only good time coming for your new friend was that first sip of booze, the heady rush of feeding an insatiable
beast. It was all down hill from there.

You shake your head - you've got bigger fish to fry and a crime scene to get to. You make your way down to the bus
station, your pockets a little lighter.
"""

    elif tree_input == 'c':
        print """
"Oh, a tough guy, eh?"

The man glances around, taking full measure of his surroundings. You quickly understand what he's searching for - other
people. To your dismay no one is close enough to prevent an altercation.

The man's disposition has shifted entirely. All trace of vulnerability has disappeared. His seemingly frail frame now
appears lean and supple. He slinks towards you, a viper ready to strike.

"A chump like you needs to be taught some manners." His hand slides towards the small of his back and, in a moment,
produces a switchblade. He presses the button on the handle and the blade springs to life.

"Besides, I know you are holding out on me."
"""
        if my_character['strength'] >= 40 or my_character['agility'] >= 40:
            print """
There's no question what the man's intentions are. It's best to pull the fuse out of this stick of dynamite before it
blows up in your face. You pull your left fist back to fake him out; he thrusts the blade towards you, which affords
you the opportunity to snatch his wrist with your right hand. A quick yank up of his wrist disarms him immediately.
Holding his wrist you spin around him and pin his arm against his back. You push up - hard - and the man cries out as he
is rendered helpless.

Now that you have his attention, it might be time to talk some sense into him. "Are you going to behave yourself,
maggot?"

"Yes. Yes!"

"Good. I don't have time to deal with your nonsense right now."

You kick away the switchblade towards the curb, unhand the man and stare him down. He gives you a baleful sneer, holding
his arm in pain.

"You better hope you don't run into me again," he says then turns and disappears around the corner.

This is definitely an inauspicious beginning to your investigation. What the hell is the world coming to when he is
almost killed right outside his office?

You shake your head - you've got bigger fish to fry and a crime scene to get to. You make your way down to the bus
station, your heart pounding in your ears.
"""
        else:
            print """
The man thrusts the blade at you - you try to dodge but he is too quick. The blade catches you right in the stomach. The
surprise of the steel puncturing your stomach is immediate and intense - you are immobilized with the shock. The man
makes quick work of you, plunging the blade in again and again. The pain explodes in your gut as the blood spills out of
you. As you slump to the ground, your senses become more distant and hollow. The pain becomes a dull ache that slips
further and further away. You are barely aware of the man standing over you, rifling through your pockets. His stench is
the last thing you connect with before you slip away for good.
"""
            death()
    else:
        print "Please enter the letter that corresponds with the dialogue you wish to choose."
        dialogue_tree()


dialogue_tree()

raw_input("Press Enter to continue...  ")


class CrimeScene(Scene):
    def enter(self):
        return 'skylark_lounge'

    print """
You arrive at the scene of the crime just as the sun is beginning to sink behind the sprawling neighborhood of Lawndale.
Though primarily Russian, Lawndale is strewn with every kind of first and second generation transplants imaginable,
creating a strange stew of language and culture. And, better yet, whenever a violent crime is committed its residents
are suddenly stricken deaf and dumb - nobody heard anything and no one talks. Sternwood was an outsider, not one of
them; what did the death of one man from the other side of the tracks matter to them?

You round the corner into the alley to be greeted by a wall of tape and three patrolmen. Seems like a pretty strong
presence, considering the scene is half a day old. You also notice, even from here, the body has been removed.

Gaining access will be tricky, at best.
"""


def dialogue_tree():
    tree_input = raw_input("""
What's your next move, ace?

A.) Wait it out.
B.) Attempt to create a diversion.
C.) ... Suppose it doesn't hurt to ask, does it?
""").lower()

    if tree_input == 'a':
        print """
Seeing as you have no legal means to enter the crime scene, you decide to wait it out and hope you'll be able to find
something that a half dozen or so other seasoned and trained law enforcement officials couldn't. Fat chance, you
suppose, but you've got nothing to go on at the moment. You could wait for the report typed out by the lead CSI and go
from there, but that could be days. Best to strike when the iron is hottest, or, in this case, best before it cools
completely.

You wait for a few hours; no one goes in, nothing comes out. The locals were steering clear, as well. What few
passerby there were gave the alley a wide berth. There were no curious onlookers, no reporters. This is perhaps the
most bizarre crime scene you've run across. Usually there is a hive of activity around a suspected homicide but this...
were they police officers collecting evidence, or merely guards preventing access? It just didn't make sense.

The police officers finally pack up and leave, plodding their way back to their squad cars. You watch them go, round
back in the alley and step under the still-hanging police tape. You use the last few minutes of daylight to search the
scene.
"""

        raw_input("Press Enter to continue...  ")

        print """
It's difficult to determine what has been removed apart from the body but, as you walk a little further, your eye
catches the glint of metal on the ground. You crouch down and look - your stomach sinks as you come face to face with an
empty shell casing.

How can this be? Such an important piece of evidence couldn't have possibly been overlooked. This can't be explained by
sloppy police work; this was intentionally left. But why?

You look behind you to make sure you aren't being watched. As far as you can tell, you are alone. Removing evidence from
a crime scene isn't the best idea and, even if you did, you'd have to eventually explain how you come across the casing
if it was ever used in court. Best to leave it, though you do recognize the caliber of the shell - it came from a .45.

There are other inconsistencies - no trace of fingerprint powder and the blood pattern is messy, like the body was
turned a few times before being carted off. This, of course, is not standard procedure. You also spy a small collection
of items near the side of the alley: a candy wrapper, a couple of coins, and a matchbook. Was the content of the
victim's pockets emptied out and discarded? What was it, exactly, that someone was searching for? You need to figure out
who the lead detective was on this case!

You look closer at the matchbook - it's for a bar, the Skylark Lounge. You've never heard of it, but it's as good as
place as any to keep looking.
"""

    elif tree_input == 'b':
        print """
You don't have the time to waste on these bozos - you need to get inside that crime scene. You figure the press wasn't
tipped off about this yet - perhaps it's time that changed.

You find a nearby payphone and call up the Tribune (collect, of course). You tell them that a 'high-profile' murder
had occurred in Lawndale, a member of the upper-crust who, having slummed it for a while, wound up dead. Then you call
the Daily News. And then the Daily Times, the Herald-American, the Sun, Chicago's American and every other tabloid and
rag you can think of. Your job done, you find a nice wall to lean on and wait for the carnage to ensue.

In about half an hour, a small army of reporters and their assistants descend on the crime scene. The police officers
look truly afraid as they walk out slowly to greet the mob. The reporters are ravenous for details and their shouts
drown out everything else. The officers are thoroughly distracted.

You step underneath the police tape to use what little time you have to look around before the goon squad comes
back.

It's difficult to determine what has been removed apart from the body but, as you walk a little further, your eye
catches the glint of metal on the ground. You crouch down and look - your stomach sinks as you come face to face with an
empty shell casing.
"""
        raw_input("Press Enter to continue...  ")
        print """
How can this be? Such an important piece of evidence couldn't have possibly been overlooked. This can't be explained by
sloppy police work; this was intentionally left. But why?

You look behind you to make sure you aren't being watched. As far as you can tell, the officers are still distracted.
Removing evidence from a crime scene isn't the best idea and, even if you did, you'd have to eventually explain how you
come across the casing if it was ever used in court. Best to leave it, though you do recognize the caliber of the shell
- it came from a .45.

There are other inconsistencies - no trace of fingerprint powder and the blood pattern is messy, like the body was
turned a few times before being carted off. This, of course, is not standard procedure. You also spy a small collection
of items near the side of the alley: a candy wrapper, a couple of coins, and a matchbook. Was the content of the
victim's pockets emptied out and discarded? What was it, exactly, that someone was searching for? You need to figure out
who the lead detective was on this case!

You look closer at the matchbook - it's for a bar, the Skylark Lounge. You've never heard of it, but it's as good as
place as any to keep looking. You slip away, unseen...
"""

    elif tree_input == 'c':
        print """
You walk right up to the officers. "Say, fellas - I was hired as a private investigator by the widow of the deceased. Do
you mind if I come in and have a look around? For the investigation?"
"""
        if my_character['luck'] >= 40:
            print """
Your extraordinary luck gives you an advantage in this situation: It appears the officer is about to tell you off, but
just then a woman runs screaming past the alley, followed by a man. The man notices the police officers in the alley,
stops like a deer in the headlights, and scrambles in the opposite direction. Of course all three officers abandon the
crime scene, in hot pursuit of the man. What appeared to be an impossible situation before has suddenly turned to your
favor. You step underneath the police tape to use what little time you have to look around before the goon squad comes
back.

It's difficult to determine what has been removed apart from the body but, as you walk a little further, your eye
catches the glint of metal on the ground. You crouch down and look - your stomach sinks as you come face to face with an
empty shell casing.

How can this be? Such an important piece of evidence couldn't have possibly been overlooked. This can't be explained by
sloppy police work; this was intentionally left. But why?
"""
            raw_input("Press Enter to continue...  ")
            print """
You look behind you to make sure you aren't being watched. As far as you can tell, you are alone. Removing evidence from
a crime scene isn't the best idea and, even if you did, you'd have to eventually explain how you come across the casing
if it was ever used in court. Best to leave it, though you do recognize the caliber of the shell - it came from a .45.

There are other inconsistencies - no trace of fingerprint powder and the blood pattern is messy, like the body was
turned a few times before being carted off. This, of course, is not standard procedure. You also spy a small collection
of items near the side of the alley: a candy wrapper, a couple of coins, and a matchbook. Was the content of the
victim's pockets emptied out and discarded? What was it, exactly, that someone was searching for? You need to figure out
who the lead detective was on this case!

You look closer at the matchbook - it's for a bar, the Skylark Lounge. You've never heard of it, but it's as good as
place as any to keep looking.
"""
    else:
        print "Please enter the letter that corresponds with the dialogue you wish to choose."
        dialogue_tree()


dialogue_tree()

raw_input("Press Enter to continue...  ")


class SkylarkLounge(Scene):
    def enter(self):
        return 'bar_stool'

    print """
Luckily for you the Skylark Lounge is a mere twelve blocks away. The bad news, however, is that you will have to stroll
through one of the meanest neighborhoods in Chicago, where the kids have to form gangs just to get the respect to walk
down the street. You figured you didn't stick out like a sore thumb but, not being a community member yourself, you are
(at best) an unwanted presence. It was just that 'at worst' part you didn't really care to think about as make your way
to the Lounge. Lawndale was the quintessential working class immigrant neighborhood, all frame cottages and brick
two-flats with corner and 'middle of the block stores' dashed in haphazardly. Kids play war in the front yards while
groups of men sit on their porches, regarding you with a forthright vigilance. It was all just a silent message you
read loud and clear but, still, you begin to sweat bullets. It makes you as jumpy as a puppet on a string being such
an easy target. These people, if it was their will, could easily swallow you up and no one would be the wiser. You
certainly have no intentions of adding fuel to the fire; you give the men a little nod to acknowledge your respect or
their turf. Thankfully you don't notice anyone following you as you keep your eyes on the sidewalk and keep moving.

The entrance to the Lounge is unassuming and low-key. There are no young punks outside nor is there any loud music
pouring out. In fact you probably would have walked right by it and never had known it was there if not for the half lit
neon sign above the entrance.

Despite outward appearances...
"""


class BarStool(Scene):  # random encounter
    def enter(self):
        return 'office_return'

    print ("*more text*")
    clues_found("")

class OfficeReturn(Scene):
    def enter(self):
        print ("*more_text*")
        return 'hotel_albatross'
    framed('murder_weapon')

class HotelAlbatross(Scene):
    def enter(self):
        print ("*more_text*")
        return 'hotel_room'
    clues_found("")

class HotelRoom(Scene):
    def enter(self):
        print ("*more text*")
        return 'tenement_building'
    framed('wallet')

class TenementBuilding(Scene):
    def enter(self):
        print ("*more text*")
        return 'tenement_hallway'


class TenementHallway(Scene):
    def enter(self):
        print ("*more text*")
        return 'apartment_403'


class Apartment403(Scene):
    def enter(self):
        print ("*more text*")
        return 'train_station'
    clues_found("")
    framed('contracts')

class TrainStation(Scene):
    def enter(self):
        print ("*more text*")
        return 'lawyer_office_building'
    clues_found("")


class LawyerOfficeBuilding(Scene):
    def enter(self):
        print ("*more text*")
        return 'secretary_office'
    framed("")
    check_lose()

class SecretaryOffice(Scene):
    def enter(self):
        print ("*more text*")
        return 'lawyer_office'


class LawyerOffice(Scene):
    def enter(self):
        print ("*more text*")
        return 'entrance_casino'
    clues_found("")

class EntranceCasino(Scene):
    def enter(self):
        print ("*more text*")
        return 'casino_floor'
    framed("")
    check_lose()

class CasinoFloor(Scene):
    def enter(self):
        print ("*more text*")
        return 'blackjack_table'


class BlackjackTable(Scene):
    def enter(self):
        print ("*more text*")
        return 'penthouse_suite'


class PenthouseSuite(Scene):
    def enter(self):
        print ("*more text*")
        return 'ending'
    framed("")
    check_lose()

class Ending(Scene):
    def enter(self):
        print ("*end text*")
        exit(1)


class Map(object):
    scenes = {
        'office': Office(),
        'office_building': OfficeBuilding(),
        'city_street': CityStreet(),
        'crime_scene': CrimeScene(),
        'skylark_lounge': SkylarkLounge(),
        'bar_stool': BarStool(),
        'office_return': OfficeReturn(),
        'hotel_albatross': HotelAlbatross(),
        'hotel_room': HotelRoom(),
        'tenement_building': TenementBuilding(),
        'tenement_hallway': TenementHallway(),
        'apartment_403': Apartment403(),
        'train_station': TrainStation(),
        'lawyer_office_building': LawyerOfficeBuilding(),
        'secretary_office': SecretaryOffice(),
        'lawyer_office': LawyerOffice(),
        'entrance_casino': EntranceCasino(),
        'casino_floor': CasinoFloor(),
        'blackjack_table': BlackjackTable(),
        'penthouse_suite': PenthouseSuite(),
        'ending': Ending()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


def play(game_map):
    current_scene = game_map.opening_scene()

    while True:
        next_scene_name = current_scene.enter()
        current_scene = game_map.next_scene(next_scene_name)


game_map = Map('office')
play(game_map)
