from typing import List

class LongestIncreasingSubsequence:

    def lengthOfLisHelper(self, nums: List[int], st: int, en: int, ans_map: dict) -> None:

        if st == en-1:
            ans_map[st] = 1
        compare_max = [1]
        for i in range(st + 1, en):

            if nums[i] > nums[st]:
                compare_max.append(1 + ans_map[i])
        
        ans_map[st] = max(compare_max)

    def lengthOfLIS(self, nums: List[int]) -> int:
        
        answer_map = {}
        
        for i in reversed(range(len(nums))):
            self.lengthOfLisHelper(nums, i, len(nums), answer_map)
        return max(list(answer_map.values()))


def test_length_of_lis():
    ts = LongestIncreasingSubsequence()
    answer = ts.lengthOfLIS([10,9,2,5,3,7,101,18])
    assert answer == 4
    answer = ts.lengthOfLIS([0,1,0,3,2,3])
    assert answer == 4
    answer = ts.lengthOfLIS([7,7,7,7,7,7,7])
    assert answer == 1
    answer = ts.lengthOfLIS([1,3,6,7,9,4,10,5,6])
    assert answer == 6


if __name__ == "__main__":
    test_length_of_lis()

