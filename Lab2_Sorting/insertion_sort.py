def insertion_sort(list_to_sort):
    for j in range(1,len(list_to_sort)):
        key = list_to_sort[j]
        last_sorted = j-1
        while last_sorted>=0 and list_to_sort[last_sorted] > key:
            list_to_sort[last_sorted +1] = list_to_sort[last_sorted]
            last_sorted -= 1
        list_to_sort[last_sorted +1]= key

