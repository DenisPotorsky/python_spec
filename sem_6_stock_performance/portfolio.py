def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    sum_ = 0
    global _initial_cost
    _initial_cost = prices.copy()
    for value_1, value_2 in zip(stocks.values(), prices.values()):
        sum_ += value_1 * value_2
    return sum_


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return (current_value - initial_value) / initial_value * 100


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    profit = {}
    for key, value_1, value_2 in zip(stocks.keys(), _initial_cost.values(), prices.values()):
        profit[key] = calculate_portfolio_return(float(value_1), float(value_2))
    return ''.join([i for i in profit if profit[i] == max(profit.values())])


if __name__ == "__main__":
    stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
    stocks_2 = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices_2 = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}

    print('В результате работы функции calculate_portfolio_value получаем общую стоимость портфеля акций: ',
          calculate_portfolio_value(stocks, prices))
    print(f'В результате работры функции calculate_portfolio_return получаем процент дохода портфеля: '
          f'{calculate_portfolio_return(10000, 15000)}%')
    print('В результате работы функции get_most_profitable_stock получаем символ наиболее прибыльной акции: ',
          get_most_profitable_stock(stocks_2, prices_2))
