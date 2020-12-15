def get_row(line):   
    top = 127
    bot = 0
    for char in line:
        if(char == 'F'):
            top = (top + bot) // 2
        else:
            bot = (top + bot + 1) // 2
    if(top == bot): return top

def get_column(line):
    top = 7
    bot = 0
    for char in line:
        if(char == 'L'):
            top = (top + bot) // 2
        else:
            bot = (top + bot + 1) // 2
    if(top == bot): return top

if __name__ == '__main__':
    ID_list = []
    with open("Day5.in") as f:
        for line in f:
            line = line.rstrip()
            row = get_row(line[:7])
            column = get_column(line[-3:])
            ID = row * 8 + column
            ID_list.append(ID)            
        print("Star 1:", max(ID_list), "(Maximum ID)")
        ID_list.sort()
        missing = min(ID_list)
        for elem in ID_list:
            if missing not in ID_list:
                print("Star 2:", missing, "(Missing ID)")
            missing += 1