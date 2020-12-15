def get_map():
    seat_map = []
    input_list = [line.rstrip() for line in open("Day11.in", "r").readlines()]
    for elem in input_list:
        seat_map.append(list(elem))
    return seat_map

def modify_map(seat_map):
    old = seat_map.copy()
    new = []
    while True:
        for line in old:
            new.append(line.copy())
        for i in range(len(old)):
            for j in range(len(old[i])):
                if old[i][j] == 'L' and is_occupated(old, i, j) == 0: new[i][j] = '#'
                elif old[i][j] == '#' and is_occupated(old, i, j) >= 4: new[i][j] = 'L'
        if old == new: return new
        else:
            old = new.copy()
            new.clear() 

def count_occupied(seat_map):
    counter = 0
    for line in seat_map:
        for char in line:
            if char == '#': counter += 1
    return counter

def is_occupated(seat_map, i, j):
    counter = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if not (dx == 0 and dy == 0) and i+dx >= 0 and i+dx < len(seat_map) and j+dy >= 0 and j+dy < len(seat_map[i+dx]):
                if seat_map[i+dx][j+dy] == '#':
                    counter += 1
    return counter

def modify_map_direction(seat_map):
    old = seat_map.copy()
    new = []
    while True:
        for line in old:
            new.append(line.copy())
        for i in range(len(old)):
            for j in range(len(old[i])):
                if old[i][j] == 'L' and is_occupated_direction(old, i, j) == 0: new[i][j] = '#'
                elif old[i][j] == '#' and is_occupated_direction(old, i, j) >= 5: new[i][j] = 'L'
        if old == new: return new
        else:
            old = new.copy()
            new.clear() 

def is_occupated_direction(seat_map, i, j):
    counter = 0
    length = len(seat_map[0])
    height = len(seat_map)

    dist = 0
    while (i-1-dist) >= 0 and (j-1-dist) >= 0:
        seat = seat_map[i-1-dist][j-1-dist]
        if seat == '#':
            counter += 1
            break
        if seat == 'L':
            break
        dist += 1
    
    dist = 0
    while (i-1-dist) >= 0:
        seat = seat_map[i-1-dist][j]
        if seat == '#':
            counter += 1
            break
        if seat == 'L':
            break
        dist += 1

    dist = 0
    while (i-1-dist) >= 0 and (j+1+dist) < length:
        seat = seat_map[i-1-dist][j+1+dist]
        if seat == '#':
            counter += 1
            break
        if seat == 'L':
            break
        dist += 1

    dist = 0
    while (j-1-dist) >= 0:
        seat = seat_map[i][j-1-dist]
        if seat == '#':
            counter += 1
            break
        if seat == 'L':
            break
        dist += 1
    
    dist = 0
    while (j+1+dist) < length:
        seat = seat_map[i][j+1+dist]
        if seat == '#':
            counter += 1
            break
        if seat == 'L':
            break
        dist += 1
    
    dist = 0
    while (i+1+dist) < height and (j-1-dist) >= 0:
        seat = seat_map[i+1+dist][j-1-dist]
        if seat == '#':
            counter += 1
            break
        if seat == 'L':
            break
        dist += 1
    
    dist = 0
    while (i+1+dist) < height:
        seat = seat_map[i+1+dist][j]
        if seat == '#':
            counter += 1
            break
        if seat == 'L':
            break
        dist += 1
    
    dist = 0
    while (i+1+dist) < height and (j+1+dist) < length:
        seat = seat_map[i+1+dist][j+1+dist]
        if seat == '#':
            counter += 1
            break
        if seat == 'L':
            break
        dist += 1
    return counter

if __name__ == '__main__':
    seat_map = get_map()
    modified_matrix1 = modify_map(seat_map)
    counter1 = count_occupied(modified_matrix1)
    print("Star 1:", counter1)
    modified_matrix2 = modify_map_direction(seat_map)
    counter2 = count_occupied(modified_matrix2)
    print("Star 2:", counter2)
