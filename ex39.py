#list
things=['a','b','c','d']
print things[1]

things[1]='name'
print things[1]
print things

#dict
stuff={'name':'kevin','age':25,'height':6*12+2}
print stuff['name']
print stuff['age']
print stuff['height']


print stuff.keys()

stuff[1]='kevinL'
print stuff
stuff['age']=100
print stuff

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some states
print "."*10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

print "."*10
print "Michigan's has:",cities[states['Michigan']]
print "Florida's has:",cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state,abbrev in states.items():
    print "%s is abbreviated %s" %(state,abbrev)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])


print '-' * 10
# safely get a abbreviation by state that might not be there
# state = states.get('Texas')
state = states.get('Michigan')
if not state:
    print "Sorry, no Texas."
elif state:
    print state

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city