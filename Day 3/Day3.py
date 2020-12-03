def tree_counter_function(path, index):
    if path[index] == "#":
        return 1
    else:
        return 0

def search_path(right, down):
    line_index = 0
    tree_counter = 0
    line_number = 0
    with open("Day3.in") as f:
        for line in f:
            if(line_number % down == 0):
                i = line_index % (len(line) - 1)
                tree_counter += tree_counter_function(line, i)
                line_index += right
            line_number += 1
    return tree_counter

if __name__ == "__main__":
    tc1 = search_path(1, 1)
    print("#Trees path 1:", tc1)
    tc2 = search_path(3, 1)
    print("#Trees path 2:", tc2)
    tc3 = search_path(5, 1)
    print("#Trees path 3:", tc3)
    tc4 = search_path(7, 1)
    print("#Trees path 4:", tc4)
    tc5 = search_path(1, 2)
    print("#Trees path 5:", tc5)
    print("Product between all paths:", tc1*tc2*tc3*tc4*tc5)