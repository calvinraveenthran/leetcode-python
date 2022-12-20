from typing import List
class ThreeSum:
    
    def twoSum(self, nums: List[int], pair_map: dict, st:int, en:int, answer: List[List[int]]) -> None:

        target = nums[st]
        prev_candidate = -1

        for i in range(st+1, en):
             #0 = candidate + target + nums[i]
             candidate = (-1*target) + (-1*nums[i])

             if candidate == prev_candidate:
                continue

             if candidate in pair_map and pair_map[candidate] > i:
                ans = [nums[st], nums[i], candidate]
                answer.append(ans)
                prev_candidate = candidate
 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pair_map = {}
        answer = []
        nums.sort()

        for i in range(len(nums)):
            pair_map[nums[i]] = i

        for i in range(len(nums)):

            if nums[i] > 0:
                break
            
            if i != 0 and nums[i] == nums[i-1]:
                continue

            self.twoSum(nums, pair_map, i, len(nums), answer)
        return answer

def test_three_sum():
    ts = ThreeSum()
    answer = ts.threeSum([-1,0,1,2,-1,-4])
    assert answer == [[-1,-1,2],[-1,0,1]]
    answer = ts.threeSum([0,1,1])
    assert answer == []
    answer = ts.threeSum([0,0,0,0])
    assert answer == [[0,0,0]]
    answer = ts.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4])
    assert answer == [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]


if __name__ == "__main__":
    test_three_sum()