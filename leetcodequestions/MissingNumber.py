from typing import List

class MissingNumber:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        sum = 0
        for i in range(size+1):
            sum+=i
        
        for i in range(size):
            sum-=nums[i]
        return sum

def test_missing_number():
    ts = MissingNumber()
    answer = ts.missingNumber([3,0,1])
    assert answer == 2


if __name__ == "__main__":
    test_missing_number()
