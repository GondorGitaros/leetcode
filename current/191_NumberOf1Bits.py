n = int(input("N: "))

def addDigits(num) -> int:
        num = str(num)
        counter = 0
        for i in num:
            counter += int(i)
        if counter > 9:
            addDigits(counter)
        else:
            return counter
    
print(addDigits(n))