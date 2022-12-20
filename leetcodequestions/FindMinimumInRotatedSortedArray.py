from typing import List

class FindMinimumInRotatedSortedArray:
    
    def findMin(self, nums: List[int]) -> int:
        found = False
        answer = -1
        st = 0
        en = len(nums)

        while not found:

            if st > en:
                break

            midpoint = st + int(((en - st)/2))

            if midpoint == 0:
                if nums[0] < nums[len(nums)-1]:
                    answer = midpoint
                    found = True
                    break
            else:
                if nums[midpoint - 1] > nums[midpoint]:
                    answer = midpoint
                    found = True
                    break

            if nums[midpoint] > nums[len(nums)-1]:
                st = midpoint + 1
            else:
                en = midpoint -1

        return nums[answer]

def test_find_min():
    q = FindMinimumInRotatedSortedArray()
    answer = q.findMin([3,4,5,1,2])
    assert answer == 1
    answer = q.findMin([4,5,6,7,0,1,2])
    assert answer == 0
    answer = q.findMin([11,13,15,17])
    assert answer == 11
    answer = q.findMin([5,1,2,3,4])
    assert answer == 1


if __name__ == "__main__":
    test_find_min()