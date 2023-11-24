dividend = int(input("Dividend: "))
divisor = int(input("Divisor: "))

def dividetwonums(dividend, divisor):
    counter = 0
    if dividend >= 2**31:
        return 2**31 -1
    elif dividend <= -2**31:
        return 2**31 - 1
    if dividend < 0  and divisor > 0:
        while dividend < 0:
            dividend += divisor
            counter -= 1
        return counter
    elif dividend < 0 and divisor < 0:
        while dividend < 0:
            dividend -= divisor
            counter += 1  
        return counter 
    elif dividend > 0 and divisor > 0:
        while dividend > 0:
            dividend -= divisor
            counter += 1
        return counter
    elif dividend > 0 and divisor < 0:
        while dividend > 0:
            dividend += divisor
            counter -= 1
        return counter
    elif dividend == 0:
        return 0   

print(dividetwonums(dividend, divisor))