i=0
numbers=[]

while i<6:
    print "Current i is %d" %i
    numbers.append(i)
    print numbers

    i=i+1

print "The numbers:"

for num in numbers:
    print num

exNum=[4,6,5]
print "Append exp:"
numbers.append(exNum)
print numbers
print "Extend exp:"
numbers.extend(exNum)
print numbers