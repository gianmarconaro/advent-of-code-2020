import regex

#dict for star 1
bag_dict1 = dict()
#dict for star 2
bag_dict2 = dict()

counter = 0

def check_shiny_gold_bag(carried_bags):
    for bags in carried_bags:
        if bags in bag_dict1:
            if check_shiny_gold_bag(bag_dict1[bags]):
                return True
        valid_bag = regex.match(r'shiny gold', bags)
        if valid_bag != None:
            return True
    return False

def count_bags(bags):
    counter = 0
    for bags in bag_dict2[bags]:
        counter += int(bags[0])
        if bags[1] in bag_dict2:
            counter += int(bags[0]) * count_bags(bags[1])
    return counter

if __name__ == '__main__':
    with open("Day7.in") as f:
        for line in f:
            line = line.replace(' bags', '').replace(' bag', '')
            valid_string = regex.match(r'(\D+) contain (?:(\d+) ([a-z ]+)(?:, )?)+.', line)
            if valid_string != None:
                bag = valid_string.captures(1)
                numbers = valid_string.captures(2)
                carried_bags = valid_string.captures(3)
                bag_dict1[bag[0]] = carried_bags
                bag_dict2[bag[0]] = list(zip(numbers, carried_bags))
        for key in bag_dict1:
            if check_shiny_gold_bag(bag_dict1[key]):
                counter += 1
        print("Star 1:", counter)
        print("Star 2:", count_bags('shiny gold'))