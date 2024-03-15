class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n=nums.length;
        int [] ps=new int[n] ;
        int [] pe=new int [n];
        int [] res=new int [n];
        ps[0]=nums[0];
        for (int i=1;i<n;i++){
            ps[i]=ps[i-1]*nums[i];
        }
        pe[n-1]=nums[n-1];
        for (int i=n-2;i>=0;i--){
            pe[i]=pe[i+1]*nums[i];
        }
        res[0]=pe[1];
        res[n-1]=ps[n-2];
        for (int i=1;i<n-1;i++){
            res[i]=ps[i-1]*pe[i+1];
        }
        return res;
        
    }
}
