num = int(input("num: "))

def addDigits(num):
        counter = 0
        if num < 9:
                return num
        for i in range(len(str(num))):
            print(num)
            counter += int((str(num))[i])
            num = counter
        if num < 9:
                return num
        for i in range(len(str(num))):
            print(num)
            counter += int((str(num)[i]))
            num = counter
        return num
            
                
print(addDigits(num))