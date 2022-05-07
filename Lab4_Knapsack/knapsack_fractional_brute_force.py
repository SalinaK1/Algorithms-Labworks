from knapsack_0or1_brute_force import knapsack_brute_force

def knapsack_fractional_brute_force(price_list, weight_list, max_capacity):

    solution_0or1,total_weight, maximum_profit_value, chosen_p_w_pair = knapsack_brute_force(price_list, weight_list, max_capacity)
    each_solution_profit = [0]*len(price_list)
    remaining_weight = max_capacity - total_weight

    for (index,value) in enumerate(solution_0or1):
        if value == '0':
            each_solution_profit[index] = (remaining_weight / weight_list[index]) * price_list[index]
    
    max_profit_index = each_solution_profit.index(max(each_solution_profit))
    chosen_p_w_pair.append([price_list[max_profit_index],weight_list[max_profit_index]])
    maximum_profit_value += max(each_solution_profit)
    total_weight = total_weight + remaining_weight

    print(f"The solution bit where we take the whole price and weight is {solution_0or1}. We use the fractional price for the index {max_profit_index}.")
    print(f"We take fractional price {max(each_solution_profit)} for the remaining weight {remaining_weight}.")

    return total_weight, maximum_profit_value, chosen_p_w_pair


if __name__ == '__main__':
    prices = [5,8,23,7,1,6]
    weights = [4,7,1,9,5,2]
    capacity = 15
    total_weight, maximum_profit_value, chosen_p_w_pair = knapsack_fractional_brute_force(prices,weights,capacity)
    print(f"The total weight is: {total_weight}")
    print(f"The total price is: {maximum_profit_value}") 
    print(f"The p/w pair that we choose are :{chosen_p_w_pair}")
