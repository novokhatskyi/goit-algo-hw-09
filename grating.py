from rich import print
import timeit


def find_coins_greedy(amount, coins):
    # denominations = [50, 25, 10, 5, 2, 1]
    result = {}
    total_count = 0

    for coin in coins:
        count = amount//coin
        if count > 0:
            result[coin] = count
            total_count += count
            amount -= coin * count
            count +=1

    return result, total_count


def find_min_coins(amount, coins):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    prev_coin = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev_coin[i] = coin 

    if dp[amount] == float("inf"):
        return -1, {}

    result = {}
    current = amount
    while current > 0:
        coin = prev_coin[current]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current -= coin

    return dp[amount], result

def time_for_algorithms():
    fcg = timeit.timeit(lambda: find_coins_greedy(amount, coins), number=500)
    fmc = timeit.timeit(lambda: find_min_coins(amount, coins), number=500)
    return fcg, fmc


if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    amount = int(input("Введіть суму решти: "))
    grate_greed, total_coin = find_coins_greedy(amount, coins)
    print(f"\n[bold green]Використані монети для повернення решти 'Жадібним алгоритмом':[/bold green]\n{grate_greed}")
    print(f"\n[bold blue]Загальна кількість монет для видачі решти[/bold blue]\n{total_coin}")
    t_greedy, t_dynamic = time_for_algorithms()
    print(f"\n[bold red]Час виконання розразунку функції жадібного алгоритму складає:[/bold red] {t_greedy:.6f}\n")

    total_coins_dyn, dynamic_coins = find_min_coins(amount, coins)
    print(f"\n[bold yellow]Використані монети для повернення решти 'Динамічним алгоритмом':[/bold yellow]\n{dynamic_coins}")
    print(f"\n[bold blue]Загальна кількість монет для видачі решти при динамісному алгоритмі[/bold blue]\n{total_coins_dyn}")
    print(f"\n[bold red]Час виконання розразунку функції жадібного алгоритму складає:[/bold red] {t_dynamic:.6f}\n")

    róznica = t_dynamic/t_greedy
    print(f"Різниця у часі виконання відрізняється в: {róznica:.1f} рази\n")