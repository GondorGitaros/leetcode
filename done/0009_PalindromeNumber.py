class Solution:
    def isPalindrome(self, x: int) -> bool:
        counter = 1
        boolval = False
        list = []
        x = str(x)

        for i in x:
            if i == x[-counter]:
                boolval = True
                list.append(boolval)
            else:
                boolval = False
                list.append(boolval)
            counter += 1

        if False in list:
            return False
        else:
            return True
                