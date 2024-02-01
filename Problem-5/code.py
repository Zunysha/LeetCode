class Solution(object):
    def plusOne(self, digits):
        result=int("".join(map(str,digits)))
        result=result+1
        result=list(map(int,str(result)))
        return result
digits=[1,2,3]
instance=Solution()
print(instance.plusOne(digits))