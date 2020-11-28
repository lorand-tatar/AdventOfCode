interval_start = 130254
interval_end = 678275

my_interval = range(interval_start, interval_end + 1)


def separate_digits(x):
    first = x // 100000
    second = (x - first * 100000) // 10000
    third = (x - (x // 10000) * 10000) // 1000
    fourth = (x - (x // 1000) * 1000) // 100
    fifth = (x - (x // 100) * 100) // 10
    sixth = (x - (x // 10) * 10)

    return [first, second, third, fourth, fifth, sixth]


def check_duplicate(digits):
    return (digits[0] == digits[1] and digits[1] != digits[2]) or\
           (digits[0] != digits[1] and digits[1] == digits[2] and digits[2] != digits[3]) or \
           (digits[1] != digits[2] and digits[2] == digits[3] and digits[3] != digits[4]) or \
           (digits[2] != digits[3] and digits[3] == digits[4] and digits[4] != digits[5]) or \
           (digits[3] != digits[4] and digits[4] == digits[5])


def check_non_decreasing(digits):
    return digits[0] <= digits[1] <= digits[2] <= digits[3] <= digits[4] <= digits[5]


number_of_valid_pwds = 0
for x in my_interval:
    digits = separate_digits(x)
    if check_duplicate(digits) and check_non_decreasing(digits):
        number_of_valid_pwds += 1
print("Number of valid passwords between", interval_start, "..", interval_end, ":", number_of_valid_pwds)
