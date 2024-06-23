class Solution:
	def bracketNumbers(self, str):
	    ans=[]
	    count=0
	    stack=[]
	    for i in range(len(str)):
	        if str[i]=="(":
	            count+=1
	            stack.append(count)
	            ans.append(count)
	            
	        elif str[i]==")":
	            ans.append(stack.pop())
	            
	        else:
	            continue
	    return ans
	            
