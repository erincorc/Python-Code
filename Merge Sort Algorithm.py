# MERGE SORT CODE

def mergeSort(L):
    if len(L) == 2:
        if L[0]< L[1]:
            return [L[0],L[1]]
        else:
            return [L[1],L[0]]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        return merge(left,right)

def merge(left,right):
    result = []
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i<len(left)):
        result.append(left[i])
        i += 1
    while (j<len(right)):
        result.append(right[j])
        j += 1
    return result

inp = [23,3,45,7,6,11,14,12]
print mergeSort(inp)

A = int(raw_input("Enter a number: "))
B = int(raw_input("Enter another number: "))
if A > B:
    Larger = A
else:
    Larger = B
print Larger


import random
rnd_nums = 0
odd_nums = 0
odd_target = random.randint(12,17)
while odd_nums != odd_target:
    candidate = random.randint(6,88)
    rnd_nums += 1
    if candidate%2 != 0:
        odd_nums += 1
print "It took ", rnd_nums, "random numbers to produce ", \
      odd_nums, "odd numbers"


def distance(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) == 1:
        if str1[0] == str2[0]:
            return 0
        else:
            return 1
    else:
        if str1[0] != str2[0]:
            return 1 + distance(str1[1:],str2[1:])
        else:
            return 0 + distance(str1[1:],str2[1:])
print distance('canada', 'CANadA')



def transpose(mtx):
    m = len(mtx)
    n = len(mtx[0])
    transposed = [[0 for i in range(m)] for j in range(n)]
    for x in range(m):
        for z in range(n):
            transposed[z][x] = mtx[x][z]
    return transposed

print transpose([[1,2,3],[4,5,6]])
