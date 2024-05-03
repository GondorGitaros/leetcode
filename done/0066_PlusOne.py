def plusOne(digits):
    n = ""
    for num in digits:
        n += str(num)
    n = str(int(n) + 1)
    digits = []
    for num in n:
        digits.append(int(num))

    return digits

print(plusOne([4,3,2,1]))
print(plusOne([9]))