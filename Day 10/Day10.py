def get_input():
    numbers = []
    with open("Day10.in") as f:
        for line in f:
            numbers.append(int(line))
        numbers.sort()
        numbers.insert(0, 0)
        numbers.append(max(numbers) + 3)
    return numbers

def diff(numbers, diff):
    counter = 0
    for i in range(len(numbers) - 1):
        result = numbers[i+1] - numbers[i]
        if result == diff:
            counter += 1
    return counter

def sub_lists(numbers):
    essential = []
    not_essential = []
    counter = 1
    essential.append(0)
    for i in range(len(numbers) - 1):
        if numbers[i] + 3 == numbers[i+1] and numbers[i]:
            if numbers[i] not in essential:
                essential.append(numbers[i])
            if numbers[i+1] not in essential:
                essential.append(numbers[i+1])
        if numbers[i] not in essential:
            not_essential.append(numbers[i])
    for i in range(len(essential) - 1):
        size = essential[i+1] - essential[i]
        not_essential_size = len(set(range(essential[i], essential[i+1])).intersection(set(not_essential)))
        if size > 3:
            counter *= 2**not_essential_size - 1
        else:
            counter *= 2**not_essential_size
    return counter

if __name__ == '__main__':
    numbers = get_input()
    diff1 = diff(numbers, 1)
    diff3 = diff(numbers, 3)
    print("Star 1:", diff1 * diff3)
    result = sub_lists(numbers)
    print("Star 2:", result)
