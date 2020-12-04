import re

def get_all_passports():
    all_pass_list = []
    one_pass_list = []
    with open("Day4.in") as f:
        for line in f:
            one_pass_list.append(line)
            if line == '\n':
                passport = ''.join(one_pass_list).rstrip()
                passport = passport.replace('\n', ' ')
                all_pass_list.append(passport)
                one_pass_list = []
        # in order to read the last passport
        passport = ''.join(one_pass_list).rstrip()
        passport = passport.replace('\n', ' ')
        all_pass_list.append(passport)
    return all_pass_list

def byr_condition(byr):
    if byr < 1920 or byr > 2002:
        return False
    else: return True

def iyr_condition(iyr):
    if iyr < 2010 or iyr > 2020:
        return False
    else: return True

def eyr_condition(eyr):
    if eyr < 2020 or eyr > 2030:
        return False
    else: return True

def hgt_condition(hgt, unit):
    if unit == 'cm':
        if(hgt < 150 or hgt > 193):
            return False
        else: return True
    elif unit == 'in':
        if(hgt < 59 or hgt > 76):
            return False
        else: return True
    else: return False

def ecl_condition(ecl):
    eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl not in eye_color:
        return False
    else: return True

def pid_condition(pid):
    if len(pid) != 9:
        return False
    else: return True

def check_valid_passports(passports: list):
    counter_star1 = 0
    counter_star2 = 0
    valid1 = True
    valid2 = True
    for elem in passports:

        # Star 1
        valid1 = True
        if 'byr:' not in elem: valid1 = False
        if 'iyr:' not in elem: valid1 = False
        if 'eyr:' not in elem: valid1 = False
        if 'hgt:' not in elem: valid1 = False
        if 'hcl:' not in elem: valid1 = False
        if 'ecl:' not in elem: valid1 = False
        if 'pid:' not in elem: valid1 = False
        if valid1 == True: counter_star1 += 1

        # Star 2
        valid2 = True
        formatted_string = re.search(r'byr:([0-9]+)', elem)
        if formatted_string != None:
            valid2 = byr_condition(int(formatted_string.group(1)))
            if valid2 == False: continue
        else: continue

        formatted_string = re.search(r'iyr:([0-9]+)', elem)
        if formatted_string != None:
            valid2 = iyr_condition(int(formatted_string.group(1)))
            if valid2 == False: continue
        else: continue

        formatted_string = re.search(r'eyr:([0-9]+)', elem)
        if formatted_string != None:
            valid2 = eyr_condition(int(formatted_string.group(1)))
            if valid2 == False: continue
        else: continue

        formatted_string = re.search(r'hgt:([0-9]+)(\D\D)', elem)
        if formatted_string != None:
            valid2 = hgt_condition(int(formatted_string.group(1)), formatted_string.group(2))
            if valid2 == False: continue
        else: continue

        formatted_string = re.search(r'hcl:#[0-9a-f]{6}', elem)
        if formatted_string != None: pass
        else: continue

        formatted_string = re.search(r'ecl:(\D{3})', elem)
        if formatted_string != None:
            valid2 = ecl_condition(formatted_string.group(1))
            if valid2 == False: continue
        else: continue

        formatted_string = re.search(r'pid:([0-9]+)', elem)
        if formatted_string != None:
            valid2 = pid_condition(formatted_string.group(1))
            if valid2 == False: continue
        else: continue

        if valid2: counter_star2 += 1
    return counter_star1, counter_star2

if __name__ == '__main__':
    passports = get_all_passports()
    print(check_valid_passports(passports))