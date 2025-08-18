import random
import os


def generate_domain_code():
    operator_code = "27"
    static_zeros = "000"
    random_part = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    code_without_checksum = operator_code + static_zeros + random_part
    checksum = sum(int(digit) for digit in code_without_checksum) * 10
    domain_code = f"{checksum:03d}" + code_without_checksum

    return domain_code

num_codes = 10
os.makedirs("/home/dmitriy-rudnev/Desktop/domain", exist_ok=True)

with open("/home/dmitriy-rudnev/Desktop/domain/domain_codes.txt", "w") as file:
    for _ in range(num_codes):
        code = generate_domain_code()
        file.write(code + "\n")


print(f"\nСгенерировано {num_codes} кодов и сохранено в файл.")