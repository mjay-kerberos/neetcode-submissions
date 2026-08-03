from typing import List

def read_integers() -> List[int]:
    numbers = input()
    numbers_list = numbers.split(",")
    return [int(x) for x in numbers_list]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
