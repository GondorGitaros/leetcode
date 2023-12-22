class Solution:
    def romanToInt(self, s: str) -> int:
        list = []
        for i in s:
            if i == "I":
                list.append(1)
            elif i == "V":
                list.append(5)
            elif i == "X":
                list.append(10)
            elif i == "L":
                list.append(50)
            elif i == "C":
                list.append(100)
            elif i == "D":
                list.append(500)
            elif i == "M":
                list.append(1000)
        result = 0
        counter = 1
        for i in list:
            try:
                if i < list[counter]:
                    result -= i
                else:
                    result += i
            except IndexError:
                result += i
            counter += 1  
        return result
        