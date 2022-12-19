from typing import List

class BestTimeToBuyandSellStock:
    def maxProfit(self, prices: List[int]) -> int:

        global_profit = 0

        buy = 0

        for i in range(1, len(prices)):

            profit =  prices[i] - prices[buy]

            if profit > global_profit:
                global_profit = profit
            
            if profit < 0:
                buy = i
        
        return global_profit

def test_max_profit():
    mp = BestTimeToBuyandSellStock()
    answer = mp.maxProfit([7,1,5,3,6,4])
    assert answer == 5


if __name__ == "__main__":
    test_max_profit()


