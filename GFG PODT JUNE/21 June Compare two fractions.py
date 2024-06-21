
class Solution:
    def compareFrac (self, str):
        
        # code here
        f1,f2=str.split(', ')
        v1,v2=eval(f1),eval(f2)

        if v1==v2:
            return 'equal'
        elif v1<v2:
            return f2
        else:
            return f1
            
