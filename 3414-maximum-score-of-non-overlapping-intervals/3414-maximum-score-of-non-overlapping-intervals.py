from bisect import bisect_left
class Solution:
    def maximumWeight(self, intervals):
        a = sorted((r, l, w, i) for i, (l, r, w) in enumerate(intervals))
        n = len(a)
        ends = [x[0] for x in a]
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]
        for k in range(1, 5):
            for i in range(1, n + 1):
                dp[k][i] = dp[k][i - 1]
                r, l, w, idx = a[i - 1]
                p = bisect_left(ends, l, 0, i - 1)
                score, ids = dp[k - 1][p]
                cand = (score + w, tuple(sorted(ids + (idx,))))
                if cand[0] > dp[k][i][0] or \
                   (cand[0] == dp[k][i][0] and cand[1] < dp[k][i][1]):
                    dp[k][i] = cand
        best = max(
            (dp[k][n] for k in range(1, 5)),
            key=lambda x: (x[0], tuple(-i for i in x[1]))
        )
        return list(best[1])