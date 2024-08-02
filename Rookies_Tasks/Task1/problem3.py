class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_leftmost(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) / 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def find_rightmost(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) / 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_idx = find_leftmost(nums, target)
        right_idx = find_rightmost(nums, target)

        if left_idx <= right_idx and left_idx < len(nums) and nums[left_idx] == target:
            return [left_idx, right_idx]
        else:
            return [-1, -1]
