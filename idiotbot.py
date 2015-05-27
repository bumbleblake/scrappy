import sys
import random
from datetime import datetime

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print color.YELLOW
print color.BOLD
start = "Hey, I'm Scrappy!"
print start

credit = "Created By Blake Bain"
print credit
print color.END
print color.BOLD
print color.GREEN

#Name asking
name = raw_input("What's your name: ")
#Name stupidity
namerandom = random.randint(1,2)
if namerandom == int("1"):
    print "Well, Hi there,", name[::-1]
if namerandom == int("2"):
    print "Well, uh, hi...", name

while True:
    
    now = datetime.now()
    print color.UNDERLINE
    print color.RED
    ask = raw_input("Say something to Scrappy: ")
    ask = ask.lower()
    len(ask)
        
    number = random.randint(1,26)
    print color.END
    print color.BOLD
    print color.DARKCYAN
    
    if ask == "hi" or ask =="hello":
        print "Hi."
    elif ask == "how are you?" or ask == "how are you today?":
        print "I'm good."
    elif ask == "what's the time?":
        print 'Its the year %s, %s months, %s days, %s hours, %s minutes, and %s seconds.' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    elif ask == "what's your favorite color?" or ask == "what's your favourite colour?":
        print "Triangle is my favourite color."
    elif ask == "what's your favourite fruit?":
        print "Ukelele is my favourite fruit."
    elif ask == "what sports do you play?":
        print "Soccer without a ball, and netball without a net."
    elif ask == "what video games do you play?":
        print "I play a game called Google. I still haven't mastered the 'Enter' button."
    elif ask == "where were you born?"or ask == "where are you from?":
        print "I come from the depths of your computer system. They have free coffee there!"
    elif ask == "hack":
        print "//error:335fhaitiav>>>SYSTEMHACK.ACTIVATED"
    elif ask == "258740":
        print "I dare you to try the next number up..."
    elif ask == "info":
        print "For calculator mode, use these symbols: + for plus, - for minus, * for times, / for divides, ** for powers. Do NOT use decimals. Typing 'bye' will shutdown the program."
    elif ask == "258741":
        print "You guessed the code! Oh my freakin' cheeseballs!"
    elif ask == "you spelt my name wrong" or ask == "you spelt my name backwards":
        print "Wait, did I? Nah. You must be hallucinating..."
    elif ask == "goodbye" or ask == "bye":
        print "Bye."
        print color.END
        print "Shutting down..."
        sys.exit()
    elif len(ask) > 34:
        print "Wow. That's alot to type for someone so stupid. "
    elif len(ask) > 50:
        print "Jeez, that is WAY too much to type."
    elif "+" in ask or "-" in ask or "*" in ask or "/" in ask or "**" in ask:
        print eval(ask)
    else:
        if number == int("1"):
            print "I like to fly planes too"
        if number == int("2"):
            print "How old is Sergei Borcfjerd?"
        if number == int("3"):
            print "*slaps*"
        if number == int("4"):
            print "Me too"
        if number == int("5"):
            print "*sings Tiny Tim*"
        if number == int("6"):
            print "Stop! Hammer Time!"
        if number == int("7"):
            print "Are you real?"
        if number == int("8"):
            print "Someone said that in a movie"
        if number == int("9"):
            print "What are you talking about?"
        if number == int("10"):
            print "I was about to say the same thing"
        if number == int("11"):
            print "That was the best pirate impersonation I've ever seen"
        if number == int("12"):
            print "I do not like that word."
        if number == int("13"):
            print "Since when did you start reading Harry Potter?"
        if number == int("14"):
            print "Speak louder, I'm listening to Teletubbies."
        if number == int("15"):
            print "What if I told you that Bart Simpson was voiced by a girl..."
        if number == int("16"):
            print "That's the nicest thing anyone's ever said to me!"
        if number == int("17"):
            print "Do I know you?"
        if number == int("18"):
            print "OMG. I just realised that you're George Clooney!"
        if number == int("19"):
            print "How dare you call me a tramp! I'll call the plumber if you say that once more!"
        if number == int("20"):
            print "When I was your age, we had to actually get off the couch to go potty!"
        if number == int("21"):
            print "Please speak english"
        if number == int("22"):
            print "I never knew you could speak Russian..."
        if number == int("23"):
            print "Ugh. That is disgusting."
        if number == int("24"):
            print "All this talk about chocolate is making me hungry"
        if number == int("25"):
            print "Ask me a really hard math question."
        if number == int("26"):
            print "I don't always do crappy dos equis guy impressions, but when I do, I make them even crappier than the guy who did them before me."