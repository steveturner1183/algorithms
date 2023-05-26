def fib_top_down(n, fib_memo=None):
    if fib_memo is None:
        fib_memo = {
            0: 0,
            1: 1
        }

    if n in fib_memo:
        return fib_memo[n]
    else:
        fib_memo[n] = fib_top_down(n-1, fib_memo) + fib_top_down(n-2, fib_memo)
    return fib_memo[n]


def fib_bot_up(n):
    fib_memo = {
        0: 0,
        1: 1
    }

    for i in range(2, n+1):
        fib_memo[i] = fib_memo[i-1] + fib_memo[i-2]
    return fib_memo[n]
