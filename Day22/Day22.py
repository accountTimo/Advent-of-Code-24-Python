def generate_secret_number(secret_number):
    secret_number ^= (secret_number * 64)
    secret_number %= 16777216

    secret_number ^= (secret_number // 32)
    secret_number %= 16777216

    secret_number ^= (secret_number * 2048)
    secret_number %= 16777216

    return secret_number

def calculate_2000th_secret_number(initial_secret_number):
    secret_number = initial_secret_number
    for _ in range(2000):
        secret_number = generate_secret_number(secret_number)
    return secret_number

total = 0
with open("Data.csv", "r") as file:
    for line in file.read().splitlines():

        initial_secret_number = int(line)

        result = calculate_2000th_secret_number(initial_secret_number)
        total += result

print(total)