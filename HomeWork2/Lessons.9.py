def difference(*args):
    if len(args) == 0:
        return 0
    max_num = args[0]
    min_num = args[0]
    for num in args:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    result = max_num - min_num
    return round(result, 2)
assert difference(1, 2, 3) == 2
assert difference(5, -5) == 10
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4
assert difference() == 0
print("OK")