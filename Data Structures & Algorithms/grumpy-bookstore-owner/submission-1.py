class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], k: int) -> int:
        satisfied = 0

        # customers already satisfied
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied += customers[i]

        # sliding window to compute extra customers
        window_extra = 0
        for i in range(k):
            if grumpy[i] == 1:
                window_extra += customers[i]

        max_extra = window_extra

        for i in range(k, len(customers)):
            if grumpy[i-k] == 1:
                window_extra -= customers[i-k]

            if grumpy[i] == 1:
                window_extra += customers[i]

            max_extra = max(max_extra, window_extra)

        return satisfied + max_extra
