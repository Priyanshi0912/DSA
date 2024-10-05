class Solution:
    def func(self,day,last,arr,dp):
        if day==0:
            maxi=0
            for currtask in range(3):
                if currtask!=last:
                    maxi=max(maxi,arr[0][currtask])
            return maxi
        maxi=0
        if dp[day][last]!=-1:
            return dp[day][last]
        for currtask in range(3):
            if currtask!=last:
                points=arr[day][currtask]+self.func(day-1,currtask,arr,dp)
                maxi=max(maxi,points)
        dp[day][last]= maxi
        return dp[day][last]
    def maximumPoints(self, arr, n):
        dp=[[-1]*(4) for _ in range(n+1)]
        return self.func(n-1,3,arr,dp)
        # Code here




#Tabulation

class Solution:
    def maximumPoints(self, arr, n):
        dp=[[-1]*(4) for _ in range(n+1)]
        
        dp[0][0]=max(arr[0][1],arr[0][2])
        dp[0][1]=max(arr[0][0],arr[0][2])
        dp[0][2]=max(arr[0][0],arr[0][1])
        dp[0][3]=max(arr[0][0],arr[0][1],arr[0][2])
        
        for day in range(1,n):
            for last in range(4):
                dp[day][last]=0
                for currtask in range(3):
                    if currtask!=last:
                        points=arr[day][currtask]+dp[day-1][currtask]
                        dp[day][last]=max(dp[day][last],points)
                        
        return dp[n-1][3]
