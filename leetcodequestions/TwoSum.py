from typing import List

class TwoSum:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i in range(len(nums)):
            pair_value = target - nums[i]

            if pair_value in index_map:
                return[index_map[pair_value], i]

            index_map[nums[i]] = i

def test_two_sum():
    ts = TwoSum()
    answer = ts.twoSum([2,7,11,15], 9)
    assert answer == [0,1]


if __name__ == "__main__":
    test_two_sum()
            
