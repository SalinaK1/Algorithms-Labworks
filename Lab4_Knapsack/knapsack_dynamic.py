def knapsack_dynamic(price_list, weight_list, max_capacity):

    no_of_items = len(weight_list)
    profit_table = [[0 for _ in range(max_capacity + 1)] for _ in range(no_of_items + 1)]       # profit is zero for all initially.
    chosen_p_w_pair = []
 
    for i in range(no_of_items + 1):            # see price_list and weight_list for rows
        for w in range(max_capacity + 1):           #capacities in range(max_capacity) in column so that we can write max profit for each weight.
            if i == 0 or w == 0:
                profit_table[i][w] = 0
            elif weight_list[i-1] <= w:
                profit_table[i][w] = max(price_list[i-1]
                          + profit_table[i-1][w-weight_list[i-1]], 
                              profit_table[i-1][w])
            else:
                profit_table[i][w] = profit_table[i-1][w]
 
    max_profit = profit_table[no_of_items][max_capacity]          # last element of profit table.
    total_weight = 0

    i = no_of_items             # rows of profit table
    j = max_capacity                # columns of profit table (weight)

    while i> 0 and j>0:
        if profit_table[i][j] != profit_table[i-1][j]:
            chosen_p_w_pair.append([price_list[i-1],weight_list[i-1]])
            total_weight += weight_list[i-1]
            j = j - weight_list[i-1]
        i -=1

    return total_weight, max_profit, chosen_p_w_pair
 
if __name__ == '__main__':
    prices = [5,8,23,7,1,6]
    weights = [4,7,1,9,5,2]
    capacity = 15

    total_weight, maximum_profit_value, chosen_p_w_pair = knapsack_dynamic(prices, weights, capacity)
    print(f"The total weight is: {total_weight}")
    print(f"The total price is: {maximum_profit_value}") 
    print(f"The p/w pair that we choose are :{chosen_p_w_pair}")

 