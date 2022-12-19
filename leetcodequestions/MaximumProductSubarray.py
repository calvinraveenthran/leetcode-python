from typing import List

class MaximumProductSubarray:
    def maxProduct(self, nums: List[int]) -> int:
        current_max_r = nums[0]
        potential_max_r = current_max_r

        for i in range(1, len(nums)):

            potential_max_r = potential_max_r * nums[i]

            if abs(nums[i]) > potential_max_r and abs(potential_max_r) < 2:
                potential_max_r = nums[i]
            
            if potential_max_r > current_max_r:
                current_max_r = potential_max_r
            elif nums[i] > current_max_r:
                current_max_r = nums[i]

        
        current_max_l = nums[len(nums)-1]
        potential_max_l = current_max_l

        for i in reversed(range(0, len(nums)-1)):

            potential_max_l = potential_max_l * nums[i]

            if abs(nums[i]) > potential_max_l and abs(potential_max_l) < 2:
                potential_max_l = nums[i]
            
            if potential_max_l > current_max_l:
                current_max_l = potential_max_l
            elif nums[i] > current_max_l:
                current_max_l = nums[i]

        return max(current_max_r, current_max_l)

def test_maximum__product_subarray():
    q = MaximumProductSubarray()
    answer = q.maxProduct([2,3,-2,4])
    assert answer == 6
    answer = q.maxProduct([-2,0,-1])
    assert answer == 0
    answer = q.maxProduct([-2,0,-1,1,2])
    assert answer == 2
    answer = q.maxProduct([-2,1,-1])
    assert answer == 2
    answer = q.maxProduct([2,-5,-2,-4,3])
    assert answer == 24
    answer = q.maxProduct([-1,-2,-3,0])
    assert answer == 6


if __name__ == "__main__":
    test_maximum__product_subarray()

