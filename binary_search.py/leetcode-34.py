

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)

print(first_and_last_position([5,7,7,8,8,10], 8))





# also acceptable solution
# class Solution:
#     def searchRange(self, nums: [int], target: int):
#         lower_bound = self.findBound(nums, target, True)
#         if (lower_bound == -1):
#             return [-1, -1]
#         upper_bound = self.findBound(nums, target, False)
        
#         return [lower_bound, upper_bound]
        
#     def findBound(self, nums: [int], target: int, isFirst: bool):
#         begin = 0
#         end = len(nums) - 1
#         while begin <= end:
#             mid = (begin + end) // 2    
#             if nums[mid] == target:
#                 if isFirst:
#                     if mid == begin or nums[mid-1] < target:
#                         return mid
#                     end = mid - 1
#                 else:
#                     if mid == end or nums[mid + 1] > target:
#                         return mid
#                     begin = mid + 1
#             elif nums[mid] > target:
#                 end = mid - 1
#             else:
#                 begin = mid + 1
        
#         return -1