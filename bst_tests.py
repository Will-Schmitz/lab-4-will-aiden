import sys 
import unittest 
from typing import * 
from dataclasses import dataclass 
sys.setrecursionlimit(10**6) 

from bst import * 
def cb_int(a, b)-> bool: 
    return a < b

def cb_str(a, b)-> bool:
    return a < b

def cb_point(a, b)-> bool:
    return a.dist < b.dist


class TestBST_int(unittest.TestCase):
    def test_is_empty_none(self):
        self.assertEqual(is_empty(None), True)

    def test_is_empty_node(self):
        self.assertEqual(is_empty(Node(1, None, None)), False)

    def test_insert_left(self):
        T = None
        T = insert(T, 5, cb_int)
        T = insert(T, 3, cb_int)
        self.assertEqual(T, Node(5, Node(3, None, None), None))

    def test_insert_right(self):
        T = None
        T = insert(T, 5, cb_int)
        T = insert(T, 7, cb_int)
        self.assertEqual(T, Node(5, None, Node(7, None, None)))

    def test_lookup_true(self):
        T = Node(5, Node(3, None, None), Node(7, None, None))
        self.assertEqual(lookup(T, 7, cb_int), True)

    def test_lookup_false(self):
        T = Node(5, Node(3, None, None), Node(7, None, None))
        self.assertEqual(lookup(T, 10, cb_int), False)

    def test_delete(self):
        T = Node(5, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, None, None))
        self.assertEqual(
            delete(T, 5, cb_int),
            Node(7, Node(3, Node(2, None, None), Node(4, None, None)), None)
        )


class TestBST_Alphabetical(unittest.TestCase):
    def test_is_empty_none_2(self):
        self.assertEqual(is_empty(None), True)

    def test_is_empty_node_2(self):
        self.assertEqual(is_empty(Node("a", None, None)), False)

    def test_insert_left_2(self):
        T = None
        T = insert(T, "b", cb_str)
        T = insert(T, "a", cb_str)
        self.assertEqual(T, Node("b", Node("a", None, None), None))

    def test_insert_right_2(self):
        T = None
        T = insert(T, "a", cb_str)
        T = insert(T, "b", cb_str)
        self.assertEqual(T, Node("a", None, Node("b", None, None)))

    def test_lookup_true_2(self):
        T = Node("b", Node("a", None, None), Node("b", None, None))
        self.assertEqual(lookup(T, "b", cb_str), True)

    def test_lookup_false_2(self):
        T = Node("b", Node("a", None, None), Node("c", None, None))
        self.assertEqual(lookup(T, "d", cb_str), False)

    def test_delete_2(self):
        T = Node("d", Node("b", Node("a", None, None), Node("c", None, None)), Node("e", None, None))
        self.assertEqual(
            delete(T, "d", cb_str),
            Node("e", Node("b", Node("a", None, None), Node("c", None, None)), None)
        )


class TestBST_Points(unittest.TestCase):
    def test_is_empty_none_2(self):
        self.assertEqual(is_empty(None), True)

    def test_is_empty_node_2(self):
        p1 = Point2(0, 0)
        self.assertEqual(is_empty(Node(p1, None, None)), False)

    def test_insert_left_2(self):
        p1 = Point2(0, 0)  # dist 0
        p2 = Point2(1, 0)  # dist 1
        T = None
        T = insert(T, p2, cb_point)
        T = insert(T, p1, cb_point)
        self.assertEqual(T, Node(p2, Node(p1, None, None), None))

    def test_insert_right_2(self):
        p1 = Point2(0, 0)
        p2 = Point2(1, 0)
        T = None
        T = insert(T, p1, cb_point)
        T = insert(T, p2, cb_point)
        self.assertEqual(T, Node(p1, None, Node(p2, None, None)))

    def test_lookup_true_2(self):
        p1 = Point2(0, 0)  # 0
        p2 = Point2(1, 0)  # 1
        T = Node(p2, Node(p1, None, None), Node(p2, None, None))
        self.assertEqual(lookup(T, p2, cb_point), True)

    def test_lookup_false_2(self):
        p1 = Point2(0, 0)  # 0
        p2 = Point2(1, 0)  # 1
        p3 = Point2(2, 0)  # 2
        p4 = Point2(3, 0)  # 3
        T = Node(p2, Node(p1, None, None), Node(p3, None, None))
        self.assertEqual(lookup(T, p4, cb_point), False)

    def test_delete_2(self):
        p1 = Point2(0, 0)  # 0
        p2 = Point2(1, 0)  # 1
        p3 = Point2(2, 0)  # 2
        p4 = Point2(3, 0)  # 3
        p5 = Point2(4, 0)  # 4
        T = Node(p4, Node(p2, Node(p1, None, None), Node(p3, None, None)), Node(p5, None, None))
        self.assertEqual(
            delete(T, p4, cb_point),
            Node(p5, Node(p2, Node(p1, None, None), Node(p3, None, None)), None)
        )


if __name__ == "__main__":
    unittest.main()