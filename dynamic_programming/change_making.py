import sys


def change_topdown(coins, amount, count_memo=None):
    if count_memo is None:
        count_memo = [0] * (amount + 1)

    if amount < 0:  # Change does not exist
        return -1

    elif amount == 0:  # Exact change reached
        return 0

    elif count_memo[amount] != 0:  # Stored value of change exists
        return count_memo[amount]

    else:
        minimum_coins = sys.maxsize

        for coin in coins:  # Find minimum values of sub-problems
            temp_coin_count = change_topdown(coins, amount - coin, count_memo)

            if 0 <= temp_coin_count < minimum_coins:
                minimum_coins = 1 + temp_coin_count

        if minimum_coins == sys.maxsize:  # Change does not exist
            count_memo[amount] = -1
        else:
            count_memo[amount] = minimum_coins

        return count_memo[amount]


def change_bottom_up(coins, amount):
    min_table = [amount + 1] * (amount + 1)
    min_table[0] = 0  # Set base case

    for change in range(1, amount + 1):
        for coin in coins:
            if coin <= amount and (change - coin) >= 0:
                min_change = min(min_table[change], min_table[change-coin] + 1)
                min_table[change] = min_change

    if min_table[amount] > amount:
        result = -1
    else:
        result = min_table[amount]

    return result


print(change_topdown([5, 3, 1], 9))
print(change_bottom_up([5, 3, 1], 9))