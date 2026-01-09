def digit_root(num):
    if num < 10:
        return num
    return digit_root(sum(int(digit) for digit in str(num)))
    
print(digit_root(4851))
print(digit_root(97569))
print(digit_root(889987))
