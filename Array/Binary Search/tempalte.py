# 这是单调递增的情况
def binary_search(nums: List[int], target: int) -> int:
    # 设置左右下标
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # 找到目标值
            return mid
    # 没有找到目标值
    return -1

def left_bound(nums: List[int], target: int) -> int:
    # 设置左右下标
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # 存在目标值，缩小右边界
            right = mid - 1
    # 判断是否存在目标值
    if left < 0 or left >= len(nums):
        return -1
    # 判断找到的左边界是否是目标值
    return left if nums[left] == target else -1

def right_bound(nums: List[int], target: int) -> int:
    # 设置左右下标
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # 存在目标值，缩小左边界
            left = mid + 1
    # 判断是否存在目标值
    if right < 0 or right >= len(nums):
        return -1
    # 判断找到的右边界是否是目标值
    return right if nums[right] == target else -1