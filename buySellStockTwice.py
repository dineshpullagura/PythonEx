import sys
def maxProfit():
	prices=[10,22,5,75,65,80]
	max_total_profit, min_price_so_far = 0.0, float('inf')
	first_buy_sell_profits = [0]* len(prices)	
	for i,price in enumerate(prices):
		min_price_so_far= min(min_price_so_far,price)
		max_total_profit = max(max_total_profit, price - min_price_so_far)
		first_buy_sell_profits[i]=max_total_profit

	print first_buy_sell_profits
	print prices

	max_price_so_far = float('-inf')
	for i,price in reversed(list(enumerate(prices[1:],1))):
		max_price_so_far = max(max_price_so_far,price)
		max_total_profit = max(max_total_profit, max_price_so_far - price + first_buy_sell_profits[i-1])
		print max_price_so_far,price,first_buy_sell_profits[i-1],max_total_profit,i
	print max_total_profit	
maxProfit()
