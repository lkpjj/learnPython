people=30
cars=40
buses=15

if cars>people:
    print "this is more car"
elif cars <people:
    print "this is more people"
else:
    print "the are equal"

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."