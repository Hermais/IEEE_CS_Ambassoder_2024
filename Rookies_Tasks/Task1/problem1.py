class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        for index in range(len(arr) - 1, -1, -1):
            new_value = max_right
            max_right = max(max_right, arr[index])
            arr[index] = new_value
        return arr