# PYTHON CHALLENGES
import math
from decimal import Decimal as decimal

# # Challenge 1
# def convert_minutes(minutes):
#     seconds = minutes * 60
#     print(f'{minutes} minutes == {seconds} seconds')

# convert_minutes(10)

# # Challenge 2
# def convert_seconds(seconds):
#     hours = math.trunc(seconds / 3600)
#     print(f'{seconds} minutes == {hours} hour(s)')

# convert_seconds(3600)

# Challenge 3
# list_of_numbers = [2, 9, 3, 11, 87, 22, 1, 11, 0]

# def largest_numbers(lists):
#       return max(lists, default=None)

# max_num = largest_numbers(list_of_numbers)
# print(max_num)

# Challenge 4
# product_1 = {"cost_price": 10.00,  "sell_price": 45.00,  "inventory": 400}
# product_2 = {"cost_price": 25.50,  "sell_price": 300.00,  "inventory": 200}
# product_3 = {"cost_price": 2.10,  "sell_price": 12.00,  "inventory": 1000}
# # cost_price - how much the item costs to make
# # sell_price - how much the item is priced at.
# # inventory - total amount we have in stock


# def calculate_profit(dict):
#     # cost_price * inventory = total deduction
#     total_deduction = dict['cost_price'] * dict['inventory']

#     # sell_price * inventory = total revenue
#     total_revenue = dict['sell_price'] * dict['inventory']

#     # total revenue - total deduction = profit
#     profit = decimal(total_revenue - total_deduction)
#     return round(profit, 2)


# profit_for_product_1 = calculate_profit(product_1)
# print('------------------------------')
# print(f' PROFIT FOR PRODUCT 1: ${profit_for_product_1} ')
# print('------------------------------')
# profit_for_product_2 = calculate_profit(product_2)
# print(f' PROFIT FOR PRODUCT 2: ${profit_for_product_2} ')
# print('------------------------------')
# profit_for_product_3 = calculate_profit(product_3)
# print(f' PROFIT FOR PRODUCT 3: ${profit_for_product_3}')
# print('------------------------------')

# total_profit = profit_for_product_1 + profit_for_product_2 + profit_for_product_3
# print('------------------------------')
# print(f' Total profit is ${total_profit}')
# print('------------------------------')
