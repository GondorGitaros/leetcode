dividend = int(input("Dividend: "))
divisor = int(input("Divisor: "))

def dividetwonums(dividend, divisor):
    counter = 0
    if dividend < 0:
        while dividend < 0 and divisor > 0:
            dividend += divisor
            counter -= 1
        while dividend < 0 and divisor < 0:
            dividend -= divisor
            counter += 1
        return counter
    elif dividend > 1:
        while dividend > 0 and divisor > 0:
            dividend -= divisor
            counter += 1
        while dividend > 0 and divisor < 0:
            dividend += divisor
            counter -= 1
        return counter
    elif dividend == 0:
        return 0   

print(dividetwonums(dividend, divisor))