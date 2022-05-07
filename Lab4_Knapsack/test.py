import unittest
from knapsack_0or1_brute_force import knapsack_brute_force
from knapsack_fractional_brute_force import knapsack_fractional_brute_force
from knapsack_greedy import knapsack_greedy
from knapsack_dynamic import knapsack_dynamic

class TestKnapsack(unittest.TestCase):

    def test_knapsack_0or1_brute_force(self):              #Test Assertion for 0/1 Knapsack problem (Brute Force)
        price_list1 = [55,10,47,5,4,50,8,61,85,87]
        weight_list1 = [95,4,60,32,23,72,80,62,65,46]
        max_capacity1 = 270
        
        solution1 = knapsack_brute_force(price_list1, weight_list1, max_capacity1)

        self.assertEqual(solution1[2],295)

    def test_knapsack_fractional_brute_force(self):              #Test Assertion for Fractional Knapsack problem (Brute Force)
        price_list1 = [55,10,47,5,4,50,8,61,85,87]
        weight_list1 = [95,4,60,32,23,72,80,62,65,46]
        max_capacity1 = 270
        
        solution1 = knapsack_fractional_brute_force(price_list1, weight_list1, max_capacity1)

        self.assertEqual(round(solution1[1],4),295.6944)

    def test_knapsack_greedy(self):              #Test Assertion for Fractional Knapsack problem (Greedy)
        price_list1 = [5,10,15,20,25]
        weight_list1 = [3,7,2,2,8]
        max_capacity1 = 18
        
        solution1 = knapsack_greedy(price_list1, weight_list1, max_capacity1)
        self.assertEqual(round(solution1[1],4),69.2857)

    def test_knapsack_dynamic(self):              #Test Assertion for 0/1 Knapsack problem (Dynamic Programming)
        price_list1 = [5,10,15,20,25]
        weight_list1 = [3,7,2,2,8]
        max_capacity1 = 18
        
        solution1 = knapsack_dynamic(price_list1, weight_list1, max_capacity1)
        self.assertEqual(solution1[1],65)

        price_list1 = [55,10,47,5,4,50,8,61,85,87]
        weight_list1 = [95,4,60,32,23,72,80,62,65,46]
        max_capacity1 = 270
        
        solution1 = knapsack_dynamic(price_list1, weight_list1, max_capacity1)

        self.assertEqual(solution1[1],295)

if __name__ == '__main__':
    unittest.main()
