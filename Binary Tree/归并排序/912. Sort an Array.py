class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge_sorted_arrays(left, right, merged):
            left_index, right_index, merge_index = 0, 0, 0
            # Merge the left and right arrays into the merged array
            while left_index < len(left) and right_index < len(right):
                if left[left_index] < right[right_index]:
                    merged[merge_index] = left[left_index]
                    left_index += 1
                else:
                    merged[merge_index] = right[right_index]
                    right_index += 1
                merge_index += 1

            # If there are remaining elements in left or right, add them to merged
            merged[merge_index:] = left[left_index:] if left_index < len(left) else right[right_index:]

        def merge_sort(nums):
            if len(nums) <= 1:
                return
            mid = len(nums) // 2
            left_half = nums[:mid]
            right_half = nums[mid:]

            # Recursively split and merge
            merge_sort(left_half)
            merge_sort(right_half)

            # Merge the sorted halves into the original array
            merge_sorted_arrays(left_half, right_half, nums)

            merge_sort(nums)
        return nums
        