from typing import List

class ContainerWithMostWater:
    def maxArea(self, height: List[int]) -> int:
        
        max = 0
        st = 0
        en = len(height) -1

        while st < en:

            area = (en - st)* min(height[st], height[en])
            if area > max:
                max = area
            
            if height[st] > height[en]:
                en = en -1
            else:
                st = st +1
        
        return max

def test_max_area():
    q = ContainerWithMostWater()
    answer = q.maxArea([1,8,6,2,5,4,8,3,7])
    assert answer == 49
    answer = q.maxArea([1,1])
    assert answer == 1

if __name__ == "__main__":
    test_max_area()