import sys
import random 

#print(sys.argv)
assert(len(sys.argv) == 4)
trials = int(sys.argv[1])
days   = int(sys.argv[2])
people = int(sys.argv[3])

#print((trials, days, people))

collisions = 0 
for t in range(trials):
	#create empty calender
	calendar = []
	for i in range(days):
		calendar.append(0)
	#fill with random birthday
	for i in range(people):
		bday =  random.randint(0,days-1)
		calendar[bday] +=1
	#print(calendar)
	#are there any collisions?
	found = False
	for v in calendar:
		if v>1: 
			found = True 
			break
	if found : collisions +=1	
	#add 1 if there is a collision
print(collisions/trials)
