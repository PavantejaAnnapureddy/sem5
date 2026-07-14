class Solution {
  public:
    long long factorSum(int N) {
        if (N == 1) return 1;
        
        long long sum = 1;
        int temp = N;
        
        for (int p = 2; p * p <= temp; p++) {
            if (temp % p == 0) {
                int count = 0;
                long long power = 1;
                while (temp % p == 0) {
                    temp /= p;
                    count++;
                    power *= p;
                }
                sum *= (power * p - 1) / (p - 1);
            }
        }
        
        if (temp > 1) {
            sum *= (1 + temp);
        }
        
        return sum;
    }
};