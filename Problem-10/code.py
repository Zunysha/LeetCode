class Solution(object):
    def getRow(self, rowIndex):
        tri=[]
        for i in range(rowIndex+1):
            row=[1]*(i+1)
            for j in range (1,i):
               row[j]=tri[i-1][j-1]+tri[i-1][j]
            tri.append(row)
        return tri[rowIndex]
s=Solution()
s.getRow(3)
        