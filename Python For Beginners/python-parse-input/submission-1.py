from typing import List

def read_integers() -> List[int]:
    numbers = input()
    numbers_list = numbers.split(",")
    #if int(x) for x in number_list is not used returns in ['1', '2', '3']
    return [int(x) for x in numbers_list]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
