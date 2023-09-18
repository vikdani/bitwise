from typing import List


#========== User's Code Starts Here ==========

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        d={}
        for i in arr:
            count=bin(i).count('1')
            if count not in d:
                d[count]=[i]
            else:
                d[count].append(i)
        res=[]
        for i in sorted(d.keys()):
            res.extend(d[i])
        return res                
        
    

#========== User's Code Ends Here ==========

   
    
    
    
    
    
def main():
    n=int(input())
    arr=[]
    for i in range(0,n):
        arr.append(int(input()))
    s=Solution()
    output = s.sortByBits(arr)
    string =""
    for i in range(0,n):
        string =string + str(output[i]) +" "
    print(string)
    
main()