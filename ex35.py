from sys import exit

def gold_room():
    """gold room"""
    print "This room is full of gold,how much do you take?"
    
    choice=raw_input(">")
    if "0" in choice or "1" in choice:
        how_much=int(choice)
    else:
        dead("Man,learn to type a number!")
        
    if how_much<50:
        print "Nice,you are not greedy,you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    """bear room"""
    print "This is a bear here"
    print "The bear has a bunch of honey"
    print "The fat bear is in front of anthor door."
    print "How are you going to move the bear?"
    bear_moved=False

    while True:
        choice=raw_input(">")
        if choice=="take honey":
            dead("The bear looks at you then slaps you face off.")
        elif choice=="taunt bear" and not bear_moved:
            bear_moved=True
        elif choice=="open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what you means."


def cthulhu_room():
    """just the other room"""
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice=raw_input(">")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(strings):
    print strings,"Good jobs!"
    exit(0)

def start():
    """opeart the program"""
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice=="left":
        bear_room()
    elif choice=="right":
        cthulhu_room()
    else:
        dead("You choose nothing?")

start()
"""Where program start"""