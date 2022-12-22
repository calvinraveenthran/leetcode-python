from typing import List

class FewestCoins:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        if amount == 0:
            return 0

        if amount < coins[0]:
            return -1

        ans_list =[0] + ([999999999] * (coins[0]-1))
        for i in range(coins[0], amount +1):
            current_cost = i
            min_array = []
            for j in range(len(coins)):

                coin = coins[j]
                if coin > current_cost:
                    break

                min_array.append(min([999999999, ans_list[current_cost - coin] + 1]))

            ans_list.append(min(min_array))


        if ans_list[amount] == 999999999:
            return -1
        else:
            return ans_list[amount]

def test_fewest_coins():
    ts = FewestCoins()

    answer = ts.coinChange([1,2,5], 11)
    assert answer == 3
    answer = ts.coinChange([2], 3)
    assert answer == -1
    answer = ts.coinChange([2], 1)
    assert answer == -1
    answer = ts.coinChange([1], 0)
    assert answer == 0
    answer = ts.coinChange([186,419,83,408], 6249)
    assert answer == 20
    answer = ts.coinChange([19,28,176,112,30,260,491,128,70,137,253], 8539)
    assert answer == 21
    answer = ts.coinChange([3,7,405,436], 8839)
    assert answer == 25
    answer = ts.coinChange([488,445,1,68,437,155], 1551)
    assert answer == 6


if __name__ == "__main__":
    test_fewest_coins()








