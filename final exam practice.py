# FINAL EXAM PRACTICE

s = raw_input('Enter a string of letters: ')
vowels = 'aeiou'
s = s.lower()
count = 0
new_s = ''
for x in range(len(s)):
    if s[x] in vowels:
        count += 1
    else:
        new_s = new_s + s[x]
print "Count of vowels is: ", count
print "String without any vowels in it is: ", new_s

r = ''
for y in range(len(s)):
    r = s[y] + r
print r

L = raw_input("Enter a list of strings: ")
L = L.split(',')
print L
shortest = L[0]
longest = L[0]
for element in L:
    if len(element) > len(longest):
        longest = element
    elif len(element) < len(shortest):
        shortest = element
print "Longest is ", longest, "and shortest is", shortest

import random
words = ['heck', 'hello', 'no', 'yes']
string = ''
for let in range(1,50):
    let = random.randint(97,122)
    let = chr(let)
    string = string + let
for word in words:
    if word in string:
        print word, "is in the string", string
    elif word not in string:
        print word, "is not in the string", string
        
L = [1,2,3,1,1,3,5,6,7,6,5]
print L
nodups = []
withdups = []
for element in L:
    if element in nodups:
        nodups.remove(element)
        withdups.append(element)
    else: #if element not in nodups
        nodups.append(element)
print nodups
print withdups


lst = [random.randint(0,9) for x in range(10)]
print lst
count = 0
for i in range(len(lst)):
    if lst[i] == i:
        count += 1
        print "The list element", lst[i], "matches its index of", i
print count

oddmin = 99999
oddmin_index = 0
print lst
for i in range(len(lst)):
    if i%2 == 1 and lst[i]%2 == 1 and oddmin > lst[i]:
        oddmin = lst[i]
        oddmin_index = i
print "The smallest odd element is", oddmin, "is at index", oddmin_index

