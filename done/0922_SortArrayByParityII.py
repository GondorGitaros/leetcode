class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        elist = []
        olist = []

        for i in nums:
            if i % 2 == 0:
                elist.append(i)
            else:
                olist.append(i)

        returnlist = []

        for i in range(len(elist)):
            returnlist.append(elist[i])
            returnlist.append(olist[i])

        return returnlist

        