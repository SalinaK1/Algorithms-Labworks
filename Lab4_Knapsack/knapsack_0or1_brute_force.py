def probable_solutions(n):
    '''
    bin(4) returns 0b0, 0b1, 0b10 and 0b11. We need to concatenate first two bits and insert 0 in MSB to make it of equal length.
    string.rjust(width,fill_character). 
    '''
    return [bin(x)[2:].rjust(n,'0') for x in range(2**n)]

def knapsack_brute_force(price_list, weight_list, max_capacity):

    assert len(price_list) == len(weight_list)

    number_of_items = len(weight_list)
    probable_solutions_list = probable_solutions(number_of_items)

    each_solution_profit = [0]*len(probable_solutions_list)
    chosen_p_w_pair = []

    for solution in probable_solutions_list:
        profit = sum([int(solution[i])*price_list[i] for i in range(number_of_items)])
        weight = sum([int(solution[i])*weight_list[i] for i in range(number_of_items)])

        if weight <= max_capacity:
            each_solution_profit[probable_solutions_list.index(solution)] = profit      # place the profit in the index corresponding th]o the solution's index in probable_solutions_list


    maximum_profit_value = max(each_solution_profit)
    solution_index = each_solution_profit.index(maximum_profit_value)              # equivalent to argmax in numpy. index of maximum value of list
    solution = probable_solutions_list[solution_index]

    total_weight = 0
    for (index,value) in enumerate(solution):
        if value == '1':
            total_weight += weight_list[index]
            chosen_p_w_pair.append([price_list[index],weight_list[index]])              # index of chosen items.

    
    print(f"The total weight is: {total_weight}")
    print(f"The total price is: {maximum_profit_value}") 
    print(f"The p/w pair that we choose are :{chosen_p_w_pair}")
    return solution


if __name__ == '__main__':
    prices = [5,8,23,7,1,6]
    weights = [4,7,1,9,5,2]
    capacity = 15
    print(knapsack_brute_force(prices,weights,capacity))
