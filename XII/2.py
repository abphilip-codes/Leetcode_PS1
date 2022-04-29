# 303
# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.a = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return(self.a[right]-(self.a[left-1] if(left) else 0)) 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)