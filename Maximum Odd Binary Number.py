class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        lst=list(s)
        c_1=lst.count("1")
        c_0=lst.count("0")

        if c_1==1:
            ans=(c_0)*"0" + "1"
        elif c_1>1:
            ans=(c_1 -1)*"1"+ (c_0)*"0" + "1"
        else:
            ans=(c_0)*"0"
        return ans
