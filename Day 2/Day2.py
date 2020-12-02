import re
from operator import xor

with open("input.txt") as f:

    counterStar1 = 0
    counterStar2 = 0

    for line in f:
        formattedString = re.match(r'([0-9]+)-([0-9]+)\D(\D):\D(\D+)', line)

        atLeast = int(formattedString.group(1))
        noMoreThan = int(formattedString.group(2))
        charstringToCheck = formattedString.group(3)
        stringToCheck = formattedString.group(4)
        occurrencesList = len(re.findall(charstringToCheck, stringToCheck))

        pos1 = atLeast - 1
        pos2 = noMoreThan - 1

        if occurrencesList >= atLeast and occurrencesList <= noMoreThan:
            counterStar1 += 1
            
        if xor(stringToCheck[pos1] == charstringToCheck, stringToCheck[pos2] == charstringToCheck):
            counterStar2 += 1
        
print("Star 1:", counterStar1)
print("Star 2:", counterStar2)