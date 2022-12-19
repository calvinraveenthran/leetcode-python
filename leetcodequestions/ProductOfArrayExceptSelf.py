from typing import List

class ProductOfArrayExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ones = [1] * len(nums)

        for i in range(1, len(nums)):
            ones[i] = nums[i-1]*ones[i-1]

        cumulative = 1
        for j in reversed(range(len(nums)-1)):
            cumulative = cumulative * nums[j+1]
            ones[j] = ones[j]*cumulative
        
        return ones


def test_product_except_self():
    q = ProductOfArrayExceptSelf()
    answer = q.productExceptSelf([1,2,3,4])
    assert answer == [24,12,8,6]

    answer = q.productExceptSelf([-1,1,0,-3,3])
    assert answer == [0,0,9,0,0]


if __name__ == "__main__":
    test_product_except_self()


