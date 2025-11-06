import sys 
import unittest 
from typing import * 
from dataclasses import dataclass 
sys.setrecursionlimit(10**6) 

from bst import * 

class BSTTests(unittest.TestCase): 


    def test_insert_int(self):
        def comes_before_int(num1 : int, num2: int) -> bool:
            return num1 < num2
        
        BinarySearchTree.comes_before = comes_before_int

        BT_test_1 = None

        BT_comp_1: BinTree = Node(1,None,None)

        self.assertEqual(BT_comp_1,insert(BT_test_1,1))

    
if (__name__ == '__main__'): 
    unittest.main() 