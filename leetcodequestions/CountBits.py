
class CountBits:
    def hammingWeight(self, n:int):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            n, cnt = n & (n-1), cnt + 1
        return cnt

    def countBits(self, n:int) -> list:
        """
        :type n: int
        :rtype: int
        """
        answer = []
        for n in range(n+1):
            answer.append(self.hammingWeight(n))
        return answer

def test_count_bits():
    ts = CountBits()
    answer = ts.countBits(5)
    import pdb; pdb.set_trace()
    assert answer == [0,1,1,2,1,2]

if __name__ == "__main__":
    test_count_bits()

