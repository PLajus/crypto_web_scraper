def filter_coins(coins, required_coins):
    data = []
    for coin in coins:
        if coin[1] in required_coins:
            data.append(coin)

    return data
