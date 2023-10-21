class Solution(object):
    def twoSum(self, nums, target):
        first_index = 0
        last_index = 0
        for current_index in range(len(nums)):
            difference_value = target - nums[current_index]
            if difference_value in nums[current_index+1:]:
                first_index = current_index
            if (target == (nums[first_index] + nums[current_index])):
                last_index = current_index
        if not last_index:
            return [-1, -1]
        return [first_index, last_index]


solution_object = Solution()
print("First and last index", solution_object.twoSum(
    nums=[2, 7, 11, 15], target=9))
