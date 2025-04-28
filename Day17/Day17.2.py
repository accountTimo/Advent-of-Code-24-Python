with open("Data.csv") as file:
    lines = file.readlines()

program = list(map(int, lines[4].split(":")[1].strip().split(",")))

def get_combo_value(operand, registers):
    if operand <= 3: return operand
    return registers["ABC"[operand - 4]]

def find_solution(target, answer):
    if not target:
        return answer

    for t in range(8):
        registers = {"A": (answer << 3) | t, "B": 0, "C": 0}
        output = None

        for pointer in range(0, len(program) - 2, 2):
            op, val = program[pointer], program[pointer + 1]
            match op:
                case 0:
                    if val != 3: raise ValueError
                case 1:
                    registers["B"] ^= val
                case 2:
                    registers["B"] = get_combo_value(val, registers) % 8
                case 4:
                    registers["B"] ^= registers["C"]
                case 5:
                    output = get_combo_value(val, registers) % 8
                case 6:
                    registers["B"] = registers["A"] >> get_combo_value(val, registers)
                case 7:
                    registers["C"] = registers["A"] >> get_combo_value(val, registers)
                case _:
                    raise ValueError

        if output == target[-1]:
            res = find_solution(target[:-1], registers["A"])
            if res is not None:
                return res
    return None

solution = find_solution(program, 0)
print(solution)
