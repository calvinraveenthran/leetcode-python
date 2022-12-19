from typing import List

class MaximumSubarray:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        potential_max = current_max

        for i in range(1, len(nums)):

            potential_max = potential_max + nums[i]

            if nums[i] > potential_max:
                potential_max = nums[i]

            if potential_max > current_max:
                current_max = potential_max

        return current_max

def test_maximum_subarray():
    q = MaximumSubarray()
    answer = q.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    assert answer == 6
    answer = q.maxSubArray([1])
    assert answer == 1
    answer = q.maxSubArray([5,4,-1,7,8])
    answer = q.maxSubArray([8,-19,5,-4,20])
    assert answer == 21


if __name__ == "__main__":
    test_maximum_subarray()

