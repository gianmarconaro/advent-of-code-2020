def get_operations():
    operations = []
    with open("Day8.in") as f:
        for line in f:
            line = line.replace('\n', '')
            frammented_operation = line.split(' ')
            operations.append(frammented_operation)
        return operations

def get_acc(operations):
    acc = 0
    indices = []
    i = 0
    while i < len(operations):
        if i in indices:
            return(False, acc)
        indices.append(i)
        if operations[i][0] == 'acc':
            acc += int(operations[i][1])
            i += 1
        if operations[i][0] == 'nop':
            i += 1
        if operations[i][0] == 'jmp':
            i += int(operations[i][1])
    return (True, acc)

def substitution(operations):
    i = 0
    while i < len(operations):
        old_value = operations[i]
        if operations[i][0] == 'nop':
            operations[i] = ['jmp', operations[i][1]]
        elif operations[i][0] == 'jmp':
            operations[i] = ['nop', operations[i][1]]
        elif operations[i][0] == 'acc':
            pass
        result = get_acc(operations)
        if not result[0]:
            operations[i] = old_value
            i += 1
        else: return result[1]    

if __name__ == '__main__':
    operations = get_operations()
    # Star 1
    print("Star 1:", get_acc(operations)[1])
    # Star 2
    print("Star 2:", substitution(operations))