with open('Data.csv') as f:
    data = f.read().splitlines()

registers = {line[9]: int(line.split(':')[1]) for line in data if line.startswith('Register')}
program = list(map(int, next(line.split(':')[1].split(',') for line in data if line.startswith('Program'))))

def combo(v):
    return v if v <= 3 else registers['ABC'[v-4]]

ip, output = 0, []

while ip < len(program):
    op, val = program[ip], program[ip+1]

    match op:
        case 0 | 6 | 7:
            target = 'A' if op == 0 else 'B' if op == 6 else 'C'
            registers[target] = registers['A'] // (2 ** combo(val))
            ip += 2
        case 1:
            registers['B'] ^= val
            ip += 2
        case 2:
            registers['B'] = combo(val) % 8
            ip += 2
        case 3:
            ip = val if registers['A'] != 0 else ip + 2
        case 4:
            registers['B'] ^= registers['C']
            ip += 2
        case 5:
            output.append(str(combo(val) % 8))
            ip += 2

print(','.join(output))
