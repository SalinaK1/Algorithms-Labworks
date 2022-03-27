import unittest
from insertion_sort import insertion_sort
from merge_sort import merge_sort, merge_sublist

class TestSorting(unittest.TestCase):

    def test_insertion_sort(self):              #Test Assertion of Insertion Sort
        input_list_1 = [3,6,1,8,9,0]
        input_list_2 = [0,1,3,6,8,9]
        input_list_3 = [9,8,6,3,1,0]
        input_list_4 = [3,0,8,6,1,9]
        output_list = [0,1,3,6,8,9]

        insertion_sort(input_list_1)
        insertion_sort(input_list_2)
        insertion_sort(input_list_3)
        insertion_sort(input_list_4)

        self.assertListEqual(input_list_1,output_list)
        self.assertListEqual(input_list_2,output_list)
        self.assertListEqual(input_list_3,output_list)
        self.assertListEqual(input_list_4,output_list)

    def test_merge_sort(self):                      #Test Assertion of Merge Sort
        input1 = input_list1 = [0,1,2,3,4,5]
        input2 = input_list2 = [0,3,5,1,2,4]
        input3 = input_list3 = [3,4,5,0,1,2]
        input4 = input_list4 = [1,4,5,0,2,3]

        output_list1 = [0,1,2,3,4,5]

        merge_sublist(input1,0,2,5)
        merge_sublist(input2,0,2,5)
        merge_sublist(input3,0,2,5)
        merge_sublist(input4,0,2,5)

        merge_sort(input_list1,0,5)
        merge_sort(input_list2,0,5)
        merge_sort(input_list3,0,5)
        merge_sort(input_list4,0,5)

        self.assertListEqual(input1, output_list1)
        self.assertListEqual(input2, output_list1)
        self.assertListEqual(input3, output_list1)
        self.assertListEqual(input4, output_list1)

        self.assertListEqual(input_list1, output_list1)
        self.assertListEqual(input_list2, output_list1)
        self.assertListEqual(input_list3, output_list1)
        self.assertListEqual(input_list4, output_list1)


if __name__ == '__main__':
    unittest.main()
