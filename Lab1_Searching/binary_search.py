def binary_search(given_list, key_to_search, lower,upper):
    midpoint = (upper+lower)//2         #gives midpoint's index 
    if key_to_search == given_list[midpoint]:
        return midpoint
    elif key_to_search < given_list[midpoint] and lower <= (midpoint-1):     # see the first half of the list
        return binary_search(given_list,key_to_search,lower,midpoint-1)
    elif key_to_search > given_list[midpoint] and (midpoint+1) <= upper:     # see the second half of the list
        return binary_search(given_list,key_to_search,midpoint + 1, upper)
    else:
        return -1

if __name__ == '__main__':
    our_list = [i for i in range(1,100,2)]
    # our_list=[1,5,7,9]
    lower_index = 0
    upper_index = len(our_list) - 1
    to_search = int(input("Enter the number to search: "))
    index = binary_search(our_list, to_search, lower_index, upper_index )
    print(index)


''' 
If you just want to check whether the list contains the element or not, 
you can use list concatenation in recursive function call instead of using lower and upper index
'''

