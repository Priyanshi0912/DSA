class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits="123456789"
        ans=[]
        l,h=len(str(low)),len(str(high))
        for i in range(l,h+1):
            for j in range(10-i):
                
                num=int(digits[j:j+i])
                #print(num)
                if (num>=low and num<=high):
                    ans.append(num)
        return ans
