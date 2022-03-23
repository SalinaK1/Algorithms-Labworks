import time, random
from linear_search import linear_search
from binary_search import binary_search
from matplotlib import pyplot as plt
from collections import namedtuple

def execution_time(search_algo, *args):      #Time taken to execute a search function
    start_time = time.time()
    search_algo(*args)
    return time.time() - start_time

def fetch_size_and_time():              #Record execution time for each best and worst cases for different sizes

    size_and_time = namedtuple('size_and_time', ["size", "linear_best_time", "linear_worst_time", 
                                    "binary_best_time", "binary_worst_time"])
    execution_record = []

    for size in range(10000, 110000, 10000):                        #Gives number of iterations as well as no of elements in a list as same size is used below
        linear_sample = random.sample(range(100000), size)                  #Each element of list ranges between 0 to 10k
        binary_sample = list(range(size))

        # Linear Search (Best case: search the first element and Worst case: search the last element)
        key_to_search = linear_sample[0]
        linear_best = execution_time(linear_search, linear_sample, key_to_search)

        key_to_search = linear_sample[-1]
        linear_worst = execution_time(linear_search, linear_sample, key_to_search)

        # Binary Search (Best case: search for the middle element, worst case: search for first/last element)
        key_to_search = binary_sample[(size-1)//2]
        binary_best = execution_time(binary_search, binary_sample, key_to_search, 0, size-1)

        key_to_search = binary_sample[-1]
        binary_worst = execution_time(binary_search, binary_sample, key_to_search, 0, size-1)

        execution_record.append(size_and_time(size, linear_best, linear_worst, 
                                                binary_best, binary_worst))
    return execution_record

def plot_graph(execution_record):           #Plot graph for best and worst cases of linear and binary search
    sizes = [size_and_time.size for size_and_time in execution_record]          #list of size of all records

    fig, (linear_graph,binary_graph) = plt.subplots(nrows=2, ncols=1)

    linear_graph.set_title("Linear Search Algorithm:")
    linear_graph.set_xlabel("Input Size")
    linear_graph.set_ylabel("Execution Time")
    linear_graph.plot(sizes,[each_record.linear_best_time for each_record in execution_record],
                                                    color="Blue", label="Best Case")
    linear_graph.plot(sizes,[each_record.linear_worst_time for each_record in execution_record],
                                                    color="Orange", label="Worst Case")
    linear_graph.legend()

    binary_graph.set_title("Binary Search Algorithm:")
    binary_graph.set_xlabel("Input Size")
    binary_graph.set_ylabel("Execution Time")
    binary_graph.plot(sizes,[each_record.binary_best_time for each_record in execution_record],
                                                    color="Blue", label='Best Case')
    binary_graph.plot(sizes,[each_record.binary_worst_time for each_record in execution_record],
                                                    color="Orange", label="Worst Case")
    binary_graph.legend()

    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    execution_record = fetch_size_and_time() 
    plot_graph(execution_record)                    #Plot input-size vs execution-time graph


'''
Instead of using tuple of namedtuples,
you can also use dictionary of lists, i.e, 
a list for input sizes,
a list of linear best case time and so on.
This way you don't need to use list comprehension in plot_graph function while plotting data.
'''
    
    



    
    
