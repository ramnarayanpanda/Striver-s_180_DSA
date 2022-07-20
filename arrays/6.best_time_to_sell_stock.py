# find best time to sell stock 
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            
    return max_profit


print(maxProfit[17, 20, 11, 9, 12, 6])