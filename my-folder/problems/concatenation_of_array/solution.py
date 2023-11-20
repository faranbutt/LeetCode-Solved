class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)):
            ans = nums
            ans.append(ans[i])
        return ans