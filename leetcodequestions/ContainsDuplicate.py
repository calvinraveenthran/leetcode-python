from typing import List

class ContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> int:

        contains = set()

        for i in range(len(nums)):
            if nums[i] in contains:
                return True
            contains.add(nums[i])
        
        return False

def test_contains_duplicate():
    q = ContainsDuplicate()
    answer = q.containsDuplicate([1,2,3,1])
    assert answer == True


if __name__ == "__main__":
    test_contains_duplicate()


