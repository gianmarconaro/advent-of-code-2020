with open("Day6.in") as f:
    group = ''
    group_answer = []
    counter1 = 0
    counter2 = 0
    for line in f:
        if line != '\n':
            line = line.replace('\n', '')
            group_answer.append(set(line))
            group += line
        else:
            set1 = set(group)
            counter1 += len(set1)
            set2 = group_answer[0].intersection(*group_answer[1:])
            counter2 += len(set2)
            group_answer = []
            group = ''

    print("Star 1:", counter1)
    print("Star 2:", counter2)