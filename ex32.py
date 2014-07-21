count=[1,2,3,4,5]
fruits=['apple','pears','oranges','apricots']
change=[1,'pennies',2,'dimes',3,'quarters']

for num in count:
    print "this is count %d" %num

for fruit in fruits:
    print fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change[2:5]:
    print "I got %r" % i

elements=[]
for i in range(0,6):
    print "Adding %d to the list" %i
    elements.append(i)

for i in elements:
    print "Element was: %d" % i