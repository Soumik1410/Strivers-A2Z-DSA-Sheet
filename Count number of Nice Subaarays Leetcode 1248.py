class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Can also be done with exactly k odds = atMost(k) - atMost(k-1)
        count = 0
        odds = {}
        odds[0] = 1
        odd_count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd_count += 1
            diff = odd_count - k
            if diff in odds:
                count += odds[diff]
            odds[odd_count] = odds.get(odd_count, 0) + 1
        return count
