import unittest
from binary_search import binary_search
from linear_search import linear_search

class TestSearch(unittest.TestCase):

    def test_linear_search(self):
        search_list = [1,5,7,9,3,2,6,10,8]              #Test Assertion of Linear Search
        self.assertEqual(linear_search(search_list,5),1)
        self.assertEqual(linear_search(search_list,3),4)
        self.assertEqual(linear_search(search_list,12),-1)
        self.assertEqual(linear_search(search_list,11),-1)

    def test_binary_search(self):
        search_list = [2,5,8,12,17,22,28,31,50,57]          #Test Assertion of Binary search
        self.assertEqual(binary_search(search_list,5,0,len(search_list)-1),1)
        self.assertEqual(binary_search(search_list,22,0,len(search_list)-1),5)
        self.assertEqual(binary_search(search_list,57,0,len(search_list)-1),9)
        self.assertEqual(binary_search(search_list,15,0,len(search_list)-1),-1)
        self.assertEqual(binary_search(search_list,35,0,len(search_list)-1),-1)

if __name__ == '__main__':
    unittest.main()             #Test Runner
