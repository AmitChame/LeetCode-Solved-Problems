class Solution:
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        total = n + k - 1
        r = 2 * k

        numerator = 1
        denominator = 1

        for i in range(1, r + 1):
            numerator = numerator * (total - i + 1) % MOD
            denominator = denominator * i % MOD

        return numerator * pow(denominator, MOD - 2, MOD) % MOD