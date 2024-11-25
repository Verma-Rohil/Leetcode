class Solution(object):
    def removeDuplicates(self, nums):
        d = {}
        ans = []
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
                ans.append(nums[i])
        x  = len(ans)
        ans += ["_"] *(len(nums) - x)
        for i in range(len(nums)) :
            nums[i] = ans[i]


        return x
        