#!/usr/bin/python

import argparse

def find_max_profit(prices):

 # print(prices)
  max_profit = min(prices) - max(prices)
  if len(prices) < 2:
    return max_profit

  for s in range(1, len(prices)):
    for b in range(len(prices[0:s])):
      max_profit = max(max_profit, prices[s]-prices[b])
      # print("b, s", b, s)
      # print(f"prices[s]: {prices[s]}, prices[b]: {prices[b]}, max_profit: {max_profit}")

  return max_profit

  
  # 🔻below is from before hiatus
  # max_profit_so_far = 0

  # current_min_price_so_far = prices[0]

  
  # i = 0
  # while i < len(prices):
  #   while j <= len(prices) - 1
  #   current_min_price = int(min(prices))
  #   max_profit = max(prices)

  # while i < len(prices)
  #   if cu

  # # for i in range(0, len(arr)-1):
  # #   cur_index = i
  # #   current_min_price_so_far_index = cur_index

  # #   if arr[i] < arr[current_min_price_so_far_index]:
  # #     current_min_price_so_far_index = i

  # # prices[current_min_price_so_far_index]
  
  # return profit

  '''
  U:
  inputs:
    list of stock 'prices'
  output:
    maximum profit can be made
  constraint:
    max profit to be made from single buy and sell
    must buy first before selling 
      (has to be sequential, subtractor to gain)
    profit can not be negative

  P:
  -buy+sell=positive max number ==> substract X[any index less than i] from X[i]
  
  for each i, 
  set the cur_index = i

  set `current_min_price_so_far_index` = cur_index
 
  `max_profit_so_far` = X[i]
  profit = `current` - `current_min_price_so_far`
  
  

  '''


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))