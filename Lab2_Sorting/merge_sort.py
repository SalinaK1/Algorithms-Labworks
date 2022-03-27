'''
The merge sort is a divide-and-conquer strategy. 
The problem is divided into equal subparts recursively. {Merge_sort function does that here.}
Then, the sub-parts are merged maintaining its sorted position (sorted in corect order while merging). {Merge sublist function does that work}
'''

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
        mid = start + (end-start)//2
        merge_sort(list_to_sort,start,mid)
        merge_sort(list_to_sort, mid+1, end)
        merge_sublist(list_to_sort, start,mid,end)



'''
Merge-sublist logic:
i<l1_number and => If list1 is empty all elements of list2 can be copied directly (Directly jump to else)
j >= l2_number or => if list 2 is empty copy the contents of list 1 
or list1[i] <= list2[j
if content of list 1 is lesser then copy the contents of list 1

Order of or is maintained so that list doesn't do out of range for j (if j has exceeded length of list2 copy contents of list1 directly without checking.)
'''