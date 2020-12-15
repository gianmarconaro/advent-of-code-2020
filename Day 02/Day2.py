import re
from operator import xor

with open("Day2.in") as f:

    counter_star1 = 0
    counter_star2 = 0

    for line in f:
        formatted_string = re.match(r'([0-9]+)-([0-9]+)\D(\D):\D(\D+)', line)

        at_least = int(formatted_string.group(1))
        no_more_than = int(formatted_string.group(2))
        char_to_check = formatted_string.group(3)
        string_to_check = formatted_string.group(4)
        occurrences_list = len(re.findall(char_to_check, string_to_check))

        pos1 = at_least - 1
        pos2 = no_more_than - 1

        if occurrences_list >= at_least and occurrences_list <= no_more_than:
            counter_star1 += 1
            
        if xor(string_to_check[pos1] == char_to_check, string_to_check[pos2] == char_to_check):
            counter_star2 += 1
        
print("Star 1:", counter_star1)
print("Star 2:", counter_star2)