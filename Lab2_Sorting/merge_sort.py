def merge_sublist(list_to_sort,start,mid,end):
    l1_number = mid-start +1        #includes mid
    l2_number = end-mid
    list1 = [0]*l1_number
    list2 = [0]*l2_number
    for i in range(l1_number):
        list1[i] = list_to_sort[start+i]
    for j in range(l2_number):
        list2[j] = list_to_sort[mid+1 + j]
    i=0
    j=0
    for k in range(start,end+1):
        if i<l1_number and (j >= l2_number or list1[i] <= list2[j]):
            list_to_sort[k] = list1[i]
            i +=1
        else: 
            list_to_sort[k] = list2[j]
            j += 1


def merge_sort(list_to_sort,start,end):
    if start<end:
        mid = start + (end-start)/2
        merge_sort(list_to_sort,start,mid)
        merge_sort(list_to_sort, mid+1, end)
        merge_sublist(list_to_sort, start,mid,end)