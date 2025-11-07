import sys 
import unittest 
from typing import * 
from dataclasses import dataclass 
sys.setrecursionlimit(10**6) 

from bst import * 

class TestBST_int(unittest.TestCase):
    BinarySearchTree.comes_before = lambda a, b: a < b
    
    def test_is_empty_none(self):
        self.assertEqual(is_empty(None), True)

    def test_is_empty_node(self):
        self.assertEqual(is_empty(Node(1, None, None)), False)

    def test_insert_left(self):
        self.assertEqual(insert(insert(None, 5), 3),
                         Node(5, Node(3, None, None), None))

    def test_insert_right(self):
        self.assertEqual(insert(insert(None, 5), 7),
                         Node(5, None, Node(7, None, None)))

    def test_lookup_true(self):
        cb = BinarySearchTree.comes_before = lambda a, b: a < b
        self.assertEqual(lookup(Node(5, Node(3, None, None), Node(7, None, None)), 7,cb), True)

    def test_lookup_false(self):
        cb = BinarySearchTree.comes_before = lambda a, b: a < b
        self.assertEqual(lookup(Node(5, Node(3, None, None), Node(7, None, None)), 10,cb), False)

    def test_delete(self):
        self.assertEqual(delete(Node(5, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, None, None)), 5), Node(7, Node(3, Node(2, None, None), Node(4, None, None)), None))


    
class TestBST_Alphabetical(unittest.TestCase):
    BinarySearchTree.comes_before = lambda a, b: a < b
    
    def test_is_empty_none_2(self):
        self.assertEqual(is_empty(None), True)
    
    def test_is_empty_node_2(self):
        self.assertEqual(is_empty(Node("a", None, None)), False)
    
    def test_insert_left_2(self):
        self.assertEqual(insert(insert(None, "b"), "a"),
                         Node("b", Node("a", None, None), None))
    def test_insert_right_2(self):
        self.assertEqual(insert(insert(None, "a"), "b"),
                         Node("a", None, Node("b", None, None)))
    def test_lookup_true_2(self):
        cb = BinarySearchTree.comes_before = lambda a, b: a < b
        self.assertEqual(lookup(Node("b", Node("a", None, None), Node("b", None, None)), "b",cb), True)
        
    def test_lookup_false_2(self):
        cb = BinarySearchTree.comes_before = lambda a, b: a < b
        self.assertEqual(lookup(Node("b", Node("a", None, None), Node("c", None, None)), "d",cb), False)
        
    def test_delete_2(self):
        self.assertEqual(delete(Node("d", Node("b", Node("a", None, None), Node("c", None, None)), Node("e", None, None)), "d"), Node("e", Node("b", Node("a", None, None), Node("c", None, None)), None))

class TestBST_Points(unittest.TestCase):
    BinarySearchTree.comes_before = lambda a, b: a.dist < b.dist
    p1 : Point2 = Point2(0,0) #dist 0
    p2 : Point2 = Point2(1,0) #dist 1
    p3 : Point2 = Point2(2,0) #dist 2
    p4 : Point2 = Point2(3,0) #dist 3
    p5 : Point2 = Point2(4,0) #dist 4
    
    def test_is_empty_none_2(self):
        self.assertEqual(is_empty(None), True)
    
    def test_is_empty_node_2(self):
        p1 : Point2 = Point2(0,0) #dist 0
        self.assertEqual(is_empty(Node(p1, None, None)), False)
    
    def test_insert_left_2(self):
        p1 : Point2 = Point2(0,0) #dist 0
        p2 : Point2 = Point2(1,0) #dist 1
        self.assertEqual(insert(insert(None, p2), p1),
                         Node(p2, Node(p1, None, None), None))
    def test_insert_right_2(self):
        p1 : Point2 = Point2(0,0) #dist 0
        p2 : Point2 = Point2(1,0) #dist 1
        self.assertEqual(insert(insert(None, p1), p2),
                         Node(p1, None, Node(p2, None, None)))
    def test_lookup_true_2(self):
        p1 : Point2 = Point2(0,0) #dist 0
        p2 : Point2 = Point2(1,0) #dist 1
        cb = BinarySearchTree.comes_before = lambda a, b: a.dist < b.dist
        self.assertEqual(lookup(Node(p2, Node(p1, None, None), Node(p2, None, None)), p2,cb), True)
        
    def test_lookup_false_2(self):
        p1 : Point2 = Point2(0,0) #dist 0
        p2 : Point2 = Point2(1,0) #dist 1
        p3 : Point2 = Point2(2,0) #dist 2
        p4 : Point2 = Point2(3,0) #dist 3
        cb = BinarySearchTree.comes_before = lambda a, b: a.dist < b.dist
        self.assertEqual(lookup(Node(p2, Node(p1, None, None), Node(p3, None, None)), p4,cb), False)
        
    def test_delete_2(self):
        p1 : Point2 = Point2(0,0) #dist 0
        p2 : Point2 = Point2(1,0) #dist 1
        p3 : Point2 = Point2(2,0) #dist 2
        p4 : Point2 = Point2(3,0) #dist 3
        p5 : Point2 = Point2(4,0) #dist 4
        self.assertEqual(delete(Node(p4, Node(p2, Node(p1, None, None), Node(p3, None, None)), Node(p5, None, None)), p4), Node(p5, Node(p2, Node(p1, None, None), Node(p3, None, None)), None))    
    
    
if __name__ == "__main__":
    unittest.main()