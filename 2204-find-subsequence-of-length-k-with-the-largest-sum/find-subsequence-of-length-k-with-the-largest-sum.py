class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # get the k largest numbers with their indices
        indexed = list(enumerate(nums))
        top_k = sorted(indexed, key=lambda x: x[1], reverse=True)[:k]
        # sort them back by their original order
        top_k_sorted = sorted(top_k, key=lambda x: x[0])
        # extract just the values
        return [x[1] for x in top_k_sorted]