from typing import List


#========== User's Code Starts Here ==========

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while(n>0):
            mask=n-1
            n=n & mask
            count=count+1
    
        return count
        

#========== User's Code Ends Here ==========

   
    
    
    
    
    
def main():
    n=int(input())
    s=Solution()
    output = s.hammingWeight(n)
    print(output)
    
main()