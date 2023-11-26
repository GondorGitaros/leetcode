num = int(input("num: "))

def numberOfSteps(num):
    counter = 0
    while num != 0:
        if num % 2 == 0:
            num = num/2
            counter += 1
        else:
            num -= 1
            counter += 1
    return counter
    


print(numberOfSteps(num))