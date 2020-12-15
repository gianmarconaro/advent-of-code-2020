def check_values(first25, to_check):
    found = False
    for i in range(len(first25)):
        for j in range(len(first25)):
            if (first25[i] + first25[j] == to_check) and (i < j):
                found = True
                break
    if not found:
        return to_check
    found = False
    return 0

def contiguous_values(all_lines, aim):
    for i in range(len(all_lines)):
        contiguous_list = []
        counter = 0
        j = 0
        while counter < aim:
            contiguous_list.append(all_lines[i+j])
            counter += all_lines[i+j]
            j += 1
            if counter == aim:
                result = min(contiguous_list) + max(contiguous_list)
                return result
    return 0
        
if __name__ == '__main__':
    first25 = []
    list_valid_values = []
    all_lines = []
    counter = 0
    with open("Day9.in") as f:
        for line in f:
            all_lines.append(int(line))
            if counter < 25:
                first25.append(int(line))
                counter += 1
            else:
                to_check = int(line)
                checked_value = check_values(first25, to_check)
                if checked_value != 0:
                    list_valid_values.append(checked_value)
                else:
                    first25.pop(0)
                    first25.append(to_check)
        print("Star 1:", list_valid_values[0])
        contiguous = contiguous_values(all_lines, list_valid_values[0])
        if contiguous != 0:
            print ("Star 2:", contiguous)
                