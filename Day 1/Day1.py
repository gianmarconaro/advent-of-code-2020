# Read Input

with open("input.txt") as f:
    inputNumbers = [int(line.strip()) for line in f.readlines()]

# Solution

for i in range(len(inputNumbers)):
    for j in range(i, len(inputNumbers)):
        star1 = inputNumbers[i] + inputNumbers[j]
        if star1 == 2020:
            print("\nSTAR 1")
            print("Numbers:", inputNumbers[i], inputNumbers[j])
            print("Result:", inputNumbers[i] * inputNumbers[j])
        for k in range(j, len(inputNumbers)):
            star2 = inputNumbers[i] + inputNumbers[j] + inputNumbers[k]
            if star2 == 2020:
                print("STAR 2")
                print("Numbers:", inputNumbers[i], inputNumbers[j], inputNumbers[k])
                print("Result:", inputNumbers[i] * inputNumbers[j] * inputNumbers[k])
        