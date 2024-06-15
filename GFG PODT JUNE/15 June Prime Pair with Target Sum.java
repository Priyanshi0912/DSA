class Solution {

    // Check prime and mark the primes up to n
    static boolean[] checkPrime(int n) { 
        boolean[] prime = new boolean[n + 1];
        for (int i = 2; i <= n; i++) {
            prime[i] = true;
        }

        for (int i = 2; i <= Math.sqrt(n); i++) { 
            if (prime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    prime[j] = false;
                }
            }
        }
        return prime;
    }

    public static ArrayList<Integer> getPrimes(int n) {
        boolean[] prime = checkPrime(n);
        ArrayList<Integer> ans = new ArrayList<>();

        for (int num = 2; num <= n / 2; num++) {
            if (prime[num] && prime[n - num]) {
                ans.add(num);
                ans.add(n - num);
                return ans;
                
            }
        }
        ans.add(-1);
        ans.add(-1);
        return ans;
    }

    
}
