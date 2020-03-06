#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit_so_far = 0

  current_min_price_so_far = prices[0]

  
  i = 0
  while i < len(prices):
    while j <= len(prices) - 1
    current_min_price = int(min(prices))
    max_profit = max(prices)

  while i < len(prices)
    if cu

  # for i in range(0, len(arr)-1):
  #   cur_index = i
  #   current_min_price_so_far_index = cur_index

  #   if arr[i] < arr[current_min_price_so_far_index]:
  #     current_min_price_so_far_index = i

  # prices[current_min_price_so_far_index]
  
    

    

  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))