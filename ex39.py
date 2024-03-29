#create a mapping state to abbreviation 
states = {
	'Oregon':'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

#create the basis set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviations is: ", states['Florida']

#do it by using the states then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every states abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviation for %s." %(state, abbrev)

#print 	every cities in state
print '-' * 10
for city,abbrev in cities.items():
	print "%s has the city %s." %(city,abbrev)

#now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s." % (state, abbrev, cities[abbrev])

print '-' * 10
#safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, No Texas"

#get a city with default value
city = cities.get('TX', 'Does not exist.')
print "The city fot the state 'TX' is: %s" % city


#get a city with default value
city = cities.get('CA', 'Does not exist.')
print "The city fot the state 'TX' is: %s" % city