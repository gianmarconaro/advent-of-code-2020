# Read Input

with open("Day1.in") as f:
    input_numbers = [int(line.strip()) for line in f.readlines()]

# Solution

for i in range(len(input_numbers)):
    for j in range(i, len(input_numbers)):
        star1 = input_numbers[i] + input_numbers[j]
        if star1 == 2020:
            print("\nSTAR 1")
            print("Numbers:", input_numbers[i], input_numbers[j])
            print("Result:", input_numbers[i] * input_numbers[j])
        for k in range(j, len(input_numbers)):
            star2 = input_numbers[i] + input_numbers[j] + input_numbers[k]
            if star2 == 2020:
                print("STAR 2")
                print("Numbers:", input_numbers[i], input_numbers[j], input_numbers[k])
                print("Result:", input_numbers[i] * input_numbers[j] * input_numbers[k])
        