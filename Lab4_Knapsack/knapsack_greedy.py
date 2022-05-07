from operator import truediv

def knapsack_greedy(price_list, weight_list, max_capacity):
    p_w_ratio_list = list(map(truediv, price_list, weight_list))        #Calculate p/w ratio

    sorted_p_w_ratio_list = sorted(p_w_ratio_list, reverse=True)
    total_price = 0
    total_weight = 0
    chosen_objects = []

    for i in sorted_p_w_ratio_list:
        index = p_w_ratio_list.index(i)                 #find the index in p-w list and price as well as weight list           
        if total_weight + weight_list[index] <= max_capacity:
            total_weight += weight_list[index]
            total_price += price_list[index]
            chosen_objects.append(index)
        else:                                                      #for fractional knapsack insertion
            remaining_weight = max_capacity - total_weight
            fractional_price = p_w_ratio_list[index] * remaining_weight
            print(f"We take fractional price {fractional_price} for the remaining weight {remaining_weight}.")
            total_weight += remaining_weight
            total_price += fractional_price
            chosen_objects.append(index)
            break

    chosen_p_w_pair = [[price_list[index], weight_list[index]] for index in chosen_objects]
    
    return total_weight, total_price, chosen_p_w_pair

if __name__ == '__main__':
    prices = [5,8,23,7,1,6]
    weights = [4,7,1,9,5,2]
    capacity = 15
    total_weight, total_price, chosen_p_w_pair = knapsack_greedy(prices, weights, capacity)
    print(f"The total weight is: {total_weight}")
    print(f"The total price is: {total_price}") 
    print(f"The p/w pair that we choose are :{chosen_p_w_pair}")







