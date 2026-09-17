class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = 1000000000
        best = [INF] * n
        answer = INF
        left = 0
        current_sum = 0
        shortest = INF
        for right in range(n):
            current_sum += arr[right]
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
            if current_sum == target:
                length = right - left + 1
                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, best[left - 1] + length)
                shortest = min(shortest, length)
            if right > 0:
                best[right] = shortest
        if answer == INF:
            return -1
        return answer