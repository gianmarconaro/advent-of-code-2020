import re

directions = ['N', 'E', 'S', 'W']
current_facing = 1
x0 = 0
y0 = 0
x1 = 0
y1 = 0
x2 = 10
y2 = 1

def get_input():
    coord = []
    with open("Day12.in") as f:
        [coord.append(line.rstrip()) for line in f]
    return coord
    
def calculate_coord(direction, degree):
    global x0, y0, current_facing

    if direction == 'F':
        calculate_coord(directions[current_facing], degree)
    if direction == 'L':
        while degree > 0:
            current_facing = (current_facing - 1) % 4
            degree -= 90
    if direction == 'R':
        while degree > 0:
            current_facing = (current_facing + 1) % 4
            degree -= 90
    if direction == 'N':
        y0 += degree
    if direction == 'S':
        y0 -= degree
    if direction == 'E':
        x0 += degree
    if direction == 'W':
        x0 -= degree

def calculate_coord_waypoint(direction, degree):
    global x1, y1, x2, y2

    if direction == 'F':
        while degree > 0:
            x1 += x2
            y1 += y2
            degree -= 1
    if direction == 'L':
        while degree > 0:
            temp = x2
            x2 = -1 * y2
            y2 = temp
            degree -= 90
    if direction == 'R':
        while degree > 0:
            temp = x2
            x2 = y2
            y2 = -1 * temp
            degree -= 90
    if direction == 'N':
        y2 += degree
    if direction == 'S':
        y2 -= degree
    if direction == 'E':
        x2 += degree
    if direction == 'W':
        x2 -= degree

if __name__ == '__main__':
    coord = get_input()
    for elem in coord:
        formatted_string = re.match(r'(\D)(\d+)', elem)
        direction = formatted_string.group(1)
        degree = int(formatted_string.group(2))
        calculate_coord(direction, degree)
        calculate_coord_waypoint(direction, degree)

    result1 = abs(x0) + abs(y0)
    result2 = abs(x1) + abs(y1)
    print("Star 1:", result1)
    print("Star 2:", result2)