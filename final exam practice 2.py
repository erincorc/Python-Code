# FINAL EXAM PRACTICE 2
import random

L = [random.randint(0,99) for x in range(15)]
print L
count = 0
for x in range(len(L)):
    if L[x]%2 == 1 and x%2 == 0:
        count += 1
print count

size = int(raw_input('Size?'))
L = [[random.randint(1,10) for x in range(size)] for y in range(size)]

for row in range(0,size):
    print ""
    for col in range(0,size):
        print "%4i" %L[row][col],
print
        
# PRINTING A T:
for col in range(size):
    print L[0][col]
for row in range(1,size):
    print L[row][int(size/2)]
print

#PRINTING AN H:
for row in range(size):
    print L[row][0]
for col in range(1, size-1):
    print L[int(size/2)][col]
for row in range(size):
    print L[row][size-1]
print

#PRINTING AN X:
for i in range(size):
    print L[i][i]
for x in range(0, size, -1):
    print L[x][x]
print

# ODD AND EVEN COUNT OUTNUMBER RANDOM PROGRAM
import random
size = random.randint(10,20)
m = random.randint(50,100)
L = [random.randint(1,m) for i in range(size)]
print L
oddcount = 0
evencount = 0
numdif = random.randint(1,10)
while (oddcount - evencount) < numdif:
    for i in L:
        print i
        if i%2 == 1:
            oddcount += 1
        else:
            evencount += 1
    break
if (oddcount - evencount) < numdif:
    print "Never reached the desired difference"
else:
    print "number difference = ", numdif
    print "odd count = ", oddcount, ", even count = ", evencount
    

