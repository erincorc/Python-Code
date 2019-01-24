# removing dups in a list w/o making a new list
def remove_dups(lst):
    while len(lst) >= 0:
        for element in lst:
            count = 0
            for value in lst:
                if value == element:
                    count += 1
                    if count > 1:
                        lst.remove(value)
        return lst

import random
size = int(raw_input('List length? '))
lst = [random.randint(1,10) for x in range(size)]
print lst
print remove_dups(lst)
