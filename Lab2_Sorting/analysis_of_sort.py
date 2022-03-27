import time
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from matplotlib import pyplot as plt
from collections import namedtuple

def execution_time(sort_algo, *args):      #Time taken to execute a sort function
    start_time = time.time()
    sort_algo(*args)
    return time.time() - start_time

def fetch_size_and_time():              #Record execution time for each best and worst cases for different sizes

    size_and_time = namedtuple('size_and_time', ["size", "insertion_best_time", "insertion_worst_time", 
                                    "merge_time"])
    execution_record = []

    for size in range(10000, 110000, 10000):                        #Gives number of iterations as well as no of elements in a list as same size is used below
        sample_list = list(range(size))
        reversed_sample_list = list(reversed(range(size)))

        # Insertion sort (Best case: already sorted list and Worst case: list sorted in reversed order.)
        insertion_best = execution_time(insertion_sort, sample_list)

        insertion_worst = execution_time(insertion_sort, reversed_sample_list)

        # Merge Sort (same for all cases as it divides all arrays in two halves and combine them.)
        merge = execution_time(merge_sort, sample_list, 0, size-1)

        execution_record.append(size_and_time(size, insertion_best, insertion_worst, 
                                                merge))
    return execution_record

def plot_graph(execution_record):           #Plot graph for best and worst cases of insertion and merge sort
    sizes = [size_and_time.size for size_and_time in execution_record]          #list of size of all records

    fig, (insertion_graph,merge_graph) = plt.subplots(nrows=2, ncols=1)

    insertion_graph.set_title("Insertion Sort Algorithm:")
    insertion_graph.set_xlabel("Input Size")
    insertion_graph.set_ylabel("Execution Time")
    insertion_graph.plot(sizes,[each_record.insertion_best_time for each_record in execution_record],
                                                    color="Blue", label="Best Case")
    insertion_graph.plot(sizes,[each_record.insertion_worst_time for each_record in execution_record],
                                                    color="Orange", label="Worst Case")
    insertion_graph.legend()

    merge_graph.set_title("Merge Sort Algorithm:")
    merge_graph.set_xlabel("Input Size")
    merge_graph.set_ylabel("Execution Time")
    merge_graph.plot(sizes,[each_record.merge_time for each_record in execution_record],
                                                    color="Blue", label='Average Case')
    merge_graph.legend()

    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    execution_record = fetch_size_and_time() 
    plot_graph(execution_record)                    #Plot input-size vs execution-time graph


'''
Instead of using tuple of namedtuples,
you can also use dictionary of lists, i.e, 
a list for input sizes,
a list of insertion best case time and so on.
This way you don't need to use list comprehension in plot_graph function while plotting data.
'''
    
    



    
    
