def add_two_numbers() -> int:
    two_nums= input()
    nums = [int(x) for x in two_nums.split(",")]
    return sum(nums)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
