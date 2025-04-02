import sys
from collections import deque

sys.setrecursionlimit(10**6)

input_file = sys.argv[1] if len(sys.argv) >= 2 else 'Data.csv'

part1_result = 0
part2_result = 0

data = open(input_file).read().strip()

def solve(part2):
    item_positions = deque([])
    space_positions = deque([])
    file_id = 0
    final_positions = []
    current_position = 0

    for i, c in enumerate(data):
        if i % 2 == 0:  # Even index represents items
            if part2:
                item_positions.append((current_position, int(c), file_id))
            for _ in range(int(c)):
                final_positions.append(file_id)
                if not part2:
                    item_positions.append((current_position, 1, file_id))
                current_position += 1
            file_id += 1
        else:  # Odd index represents spaces
            space_positions.append((current_position, int(c)))
            for _ in range(int(c)):
                final_positions.append(None)
                current_position += 1

    # Move items into spaces based on size constraints
    for (pos, size, file_id) in reversed(item_positions):
        for space_index, (space_pos, space_size) in enumerate(space_positions):
            if space_pos < pos and size <= space_size:
                for i in range(size):
                    assert final_positions[pos + i] == file_id, f'{final_positions[pos + i]=}'
                    final_positions[pos + i] = None
                    final_positions[space_pos + i] = file_id
                space_positions[space_index] = (space_pos + size, space_size - size)
                break

    # Calculate the final result
    total = 0
    for i, c in enumerate(final_positions):
        if c is not None:
            total += i * c
    return total

part1_result = solve(False)
part2_result = solve(True)

print(part1_result)
print(part2_result)
