ten_thing="Apple Oranges Crows Telephone Light Sugar"
print "Wait there's not 10 things in that list,let's fix that."

stuff=ten_thing.split(' ')

print stuff

more_stuff=["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff)!=10:
    next_one=more_stuff.pop()
    print "Adding:",next_one
    stuff.append(next_one)
    print "This is %d items now." %len(stuff)

print stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
# print ' '.join(stuff)
# print '#'.join(stuff[3:5])
# print '*'.join(stuff)
_stuff='*'.join(stuff)
print _stuff

sstuff=' '.join(stuff)
print sstuff