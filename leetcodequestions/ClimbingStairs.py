class ClimbingStairs:
    def climbStairs(self, n: int) -> int:
        init_array = [0,1,2,3,5]

        if n < 5:
            return init_array[n]

        for i in range(5, n+1):
            init_array.append(init_array[i-1] + init_array[i-2])
        
        return init_array[n]

def test_climb_stairs():
    ts = ClimbingStairs()
    answer = ts.climbStairs(5)
    assert answer == 8


if __name__ == "__main__":
    test_climb_stairs()