def linear_search(our_list, key_to_search):
    for i in range(len(our_list)):
        if key_to_search == our_list[i]:
            return i
    return -1

if __name__ == '__main__':
    given_list = [i for i in range(5,100)]
    to_search = int(input("Enter the key to search: "))
    index = linear_search(given_list,to_search)
    print(index)
