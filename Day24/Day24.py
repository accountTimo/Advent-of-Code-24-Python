import re

def parse_input(filename):
    wire_values = {}
    gates = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if ':' in line:
                wire, value = line.split(':')
                wire_values[wire.strip()] = int(value.strip())
            else:
                match = re.match(r'(\w+) (AND|OR|XOR) (\w+) -> (\w+)', line)
                if match:
                    input1, op, input2, output = match.groups()
                    gates.append((input1, op, input2, output))

    return wire_values, gates

def evaluate_gates(wire_values, gates):
    pending = gates[:]
    while pending:
        next_pending = []
        for input1, op, input2, output in pending:
            if input1 in wire_values and input2 in wire_values:
                val1 = wire_values[input1]
                val2 = wire_values[input2]
                if op == "AND":
                    result = val1 & val2
                elif op == "OR":
                    result = val1 | val2
                elif op == "XOR":
                    result = val1 ^ val2
                else:
                    raise ValueError(f"Unknown operator: {op}")
                wire_values[output] = result
            else:
                next_pending.append((input1, op, input2, output))
        if len(next_pending) == len(pending):
            raise RuntimeError("Stuck in evaluation; circular dependency or missing inputs")
        pending = next_pending
    return wire_values

def extract_z_bits(wire_values):
    z_bits = [(wire, val) for wire, val in wire_values.items() if wire.startswith('z')]
    z_bits.sort(key=lambda x: int(x[0][1:]))
    binary_str = ''.join(str(val) for _, val in z_bits)
    return int(binary_str[::-1], 2)

if __name__ == "__main__":
    wire_values, gates = parse_input("Data.csv")
    wire_values = evaluate_gates(wire_values, gates)
    result = extract_z_bits(wire_values)
    print("Decimal output:", result)
