def linear_search(given_list, key_to_search):
    for i in range(len(given_list)):
        if key_to_search == given_list[i]:
            return i
    return -1

if __name__ == '__main__':
    our_list = [i for i in range(5,100)]
    to_search = int(input("Enter the key to search: "))
    index = linear_search(our_list,to_search)
    print(index)

'''
You can also use enumerate to given_list and return its index.
'''
