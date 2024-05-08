class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        

        sorted_score=sorted(score,reverse=True)
        score_index=dict()
        ans=[]
        for ele in score:
            score_index[ele]=sorted_score.index(ele)
        print(score_index)
        for ele in score:
            if score_index[ele] ==0:
                ans.append("Gold Medal")
            elif score_index[ele] ==1:
                ans.append("Silver Medal")
            elif score_index[ele] ==2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(score_index[ele]+1))
        return ans
