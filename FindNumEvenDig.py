from typing import List
class FindNumEvenDig:
    def findNumbers(self, nums: List[int]) -> int:  
        return len([x for x in nums if 1 <= x/10 <= 9 or 100 <= x/10 <= 999 or 10000 <=x/10 <= 99999])