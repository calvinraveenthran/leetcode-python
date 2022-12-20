from typing import List

class SearchInrotatedSortedArray:


    def findMin(self, nums: List[int]) -> int:
        found = False
        answer = 0
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

        return answer
    
    def search(self, nums: List[int], target: int) -> int:
        found = False
        answer = -1
        min = self.findMin(nums)

        if min == 0:
            st = 0
            en = len(nums) - 1
        elif target >= nums[min] and target <= nums[len(nums) -1]:
            st = min
            en = len(nums) -1
        elif target >= nums[0] and target <= nums[min - 1]:
            st = 0
            en = min - 1
        else:
            return -1

        while not found:

            if st > en:
                break

            midpoint = st + int(((en - st)/2))

            if nums[midpoint] == target:
                answer = midpoint
                found = True
                break

            if nums[midpoint] > target:
                en = en - 1
            else:
                st = st + 1

        return answer

def test_search():
    q = SearchInrotatedSortedArray()
    answer = q.search([4,5,6,7,0,1,2], 0)
    assert answer == 4
    answer = q.search([4,5,6,7,0,1,2], 3)
    assert answer == -1
    answer = q.search([1], 0)
    assert answer == -1
    answer = q.search([1,3], 2)
    assert answer == -1
    answer = q.search([3,1], 3)
    assert answer == 0
    answer = q.search([1], 2)
    assert answer == -1



if __name__ == "__main__":
    test_search()