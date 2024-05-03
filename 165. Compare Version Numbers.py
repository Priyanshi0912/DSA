class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1=version1.split(".")
        s2=version2.split(".")
        
        v1,v2=0,0
       
        for i in range(max(len(s1),len(s2))):
            v1= int(s1[i]) if i < len(s1) else 0
            v2= int(s2[i]) if i < len(s2) else 0
            if v1<v2:
                return -1
            elif v1>v2:
                return 1
        return 0
