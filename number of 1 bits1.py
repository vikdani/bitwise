from typing import List


#========== User's Code Starts Here ==========

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if not n:
            return True
        num = n ^ (n>>1)
        return not num & (num+1)
        

#========== User's Code Ends Here ==========

   
    
    
    
    
    
def main():
    n=int(input())
    s=Solution()
    output = s.hasAlternatingBits(n)
    if(output):
        print("true")
    else:
        print("false")
    
main()