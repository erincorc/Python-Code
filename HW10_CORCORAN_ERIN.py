# DESCRIPTION: This program reads a text file about Boston restaurants and outputs data on them
# NAME: CORCORAN, ERIN
# DATE: Dec. 4, 2017

#starter code:
f = open('restaurants.HW10.txt','r')
lines = f.readlines()
nested = [[s.lstrip().rstrip() for s in line.rstrip().split(',')] for line in lines]
print nested
print
print
print "Sample Output - Name and Reading"
for i in range(len(nested)):
    print nested[i][0], "", nested[i][4]
print

#part a - cuisine with the highest average rating and the rating
cuisines = []
for i in range(len(nested)):
    if nested[i][2] not in cuisines:
        cuisines.append(nested[i][2])
cuisine_rates = []
rate_list = []
for cuisine in cuisines:
    total = 0 #initializing total and count
    count = 0
    for i in range(len(nested)):
        if nested[i][2] == cuisine:
            count = count + 1
            total = total + float(nested[i][4])
    avg = round((total/count),2) #formula for an average
    rate_list.append(avg)
    cuisine_rates.append([cuisine, avg])
max_rate = max(rate_list)
print "The type of cuisine with the highest average rating of", max_rate, "is "
for i in range(len(cuisine_rates)):
    if cuisine_rates[i][1] == max_rate:
        print cuisine_rates[i][0]
print

#part b - the cuisine with the lowest average rating and the rating
cuisine_rates = []
rate_list = []
for cuisine in cuisines:
    total = 0
    count = 0
    for i in range(len(nested)):
        if nested[i][2] == cuisine:
            count = count + 1
            total = total + float(nested[i][4])
    avg = round((total/count),2)
    rate_list.append(avg)
    cuisine_rates.append([cuisine, avg])
min_rate = min(rate_list)
print "The type of cuisine with the lowest average rating of", min_rate, "is "
for i in range(len(cuisine_rates)):
    if cuisine_rates[i][1] == min_rate:
        print cuisine_rates[i][0]
print
    
#part c - restaurant with highest rating and rating
maxrate = nested[0][4] #initialize max rate
name_maxrate = nested[0][0]
for i in range(len(nested)):
    rating = nested[i][4]
    name_rating = nested[i][0]
    if rating > maxrate:
        maxrate = rating
        name_maxrate = name_rating
print name_maxrate, "has the highest rating of", maxrate
print

#part d - the most expensive restaurant(s) with the dollar rating
rest_list = []
max_rate = nested[0][3]
for x in range(len(nested)):
    if len(nested[x][3]) > len(max_rate): #use length of the dollar sign rating to see which has highest # dollar signs
        max_rate = nested[x][3]
for i in range(len(nested)):
    if nested[i][3] == max_rate:
        rest_list.append(nested[i][0])
print "The most expensive restaurant(s) is/are: ", rest_list, "with the dollar rating ", max_rate
print
   
#part e - the restaurant in Boston with the lowest rating
lowrate = nested[1][4] #initializing the low rating
name_lowrate = nested[1][0]
for i in range(len(nested)):
    if nested[i][1] == 'Boston': #want to know about Boston restaurants
        rating = nested[i][4]
        name_rating = nested[i][0]
        if rating < lowrate:
            lowrate = rating
            name_lowrate = name_rating
print name_lowrate, "has the lowest rating in Boston, with a rate of", lowrate
