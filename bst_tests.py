# bst_tests.py
import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

from bst import *

class TestBST_int(unittest.TestCase):
    def setUp(self):
        self.cb = lambda a, b: a < b

    def test_is_empty_none(self):
        self.assertEqual(is_empty(None), True)

    def test_is_empty_node(self):
        self.assertEqual(is_empty(Node(1, None, None)), False)

    def test_insert_left(self):
        T = None
        T = insert(T, 5, self.cb)
        T = insert(T, 3, self.cb)
        self.assertEqual(T, Node(5, Node(3, None, None), None))

    def test_insert_right(self):
        T = None
        T = insert(T, 5, self.cb)
        T = insert(T, 7, self.cb)
        self.assertEqual(T, Node(5, None, Node(7, None, None)))

    def test_lookup_true(self):
        T = Node(5, Node(3, None, None), Node(7, None, None))
        self.assertEqual(lookup(T, 7, self.cb), True)

    def test_lookup_false(self):
        T = Node(5, Node(3, None, None), Node(7, None, None))
        self.assertEqual(lookup(T, 10, self.cb), False)

    def test_delete(self):
        T = Node(5, Node(3, Node(2, None, None), Node(4, None, None)), Node(7, None, None))
        self.assertEqual(
            delete(T, 5, self.cb),
            Node(7, Node(3, Node(2, None, None), Node(4, None, None)), None)
        )

class TestBST_Alphabetical(unittest.TestCase):
    def setUp(self):
        self.cb = lambda a, b: a < b

    def test_is_empty_none_2(self):
        self.assertEqual(is_empty(None), True)

    def test_is_empty_node_2(self):
        self.assertEqual(is_empty(Node("a", None, None)), False)

    def test_insert_left_2(self):
        T = None
        T = insert(T, "b", self.cb)
        T = insert(T, "a", self.cb)
        self.assertEqual(T, Node("b", Node("a", None, None), None))

    def test_insert_right_2(self):
        T = None
        T = insert(T, "a", self.cb)
        T = insert(T, "b", self.cb)
        self.assertEqual(T, Node("a", None, Node("b", None, None)))

    def test_lookup_true_2(self):
        T = Node("b", Node("a", None, None), Node("b", None, None))
        self.assertEqual(lookup(T, "b", self.cb), True)

    def test_lookup_false_2(self):
        T = Node("b", Node("a", None, None), Node("c", None, None))
        self.assertEqual(lookup(T, "d", self.cb), False)

    def test_delete_2(self):
        T = Node("d", Node("b", Node("a", None, None), Node("c", None, None)), Node("e", None, None))
        self.assertEqual(
            delete(T, "d", self.cb),
            Node("e", Node("b", Node("a", None, None), Node("c", None, None)), None)
        )

class TestBST_Points(unittest.TestCase):
    def setUp(self):
        self.cb = lambda a, b: a.dist < b.dist
        self.p1 = Point2(0, 0)
        self.p2 = Point2(1, 0)
        self.p3 = Point2(2, 0)
        self.p4 = Point2(3, 0)
        self.p5 = Point2(4, 0)

    def test_is_empty_none_2(self):
        self.assertEqual(is_empty(None), True)

    def test_is_empty_node_2(self):
        self.assertEqual(is_empty(Node(self.p1, None, None)), False)

    def test_insert_left_2(self):
        T = None
        T = insert(T, self.p2, self.cb)
        T = insert(T, self.p1, self.cb)
        self.assertEqual(T, Node(self.p2, Node(self.p1, None, None), None))

    def test_insert_right_2(self):
        T = None
        T = insert(T, self.p1, self.cb)
        T = insert(T, self.p2, self.cb)
        self.assertEqual(T, Node(self.p1, None, Node(self.p2, None, None)))

    def test_lookup_true_2(self):
        T = Node(self.p2, Node(self.p1, None, None), Node(self.p2, None, None))
        self.assertEqual(lookup(T, self.p2, self.cb), True)

    def test_lookup_false_2(self):
        T = Node(self.p2, Node(self.p1, None, None), Node(self.p3, None, None))
        self.assertEqual(lookup(T, self.p4, self.cb), False)

    def test_delete_2(self):
        T = Node(self.p4,
                 Node(self.p2, Node(self.p1, None, None), Node(self.p3, None, None)),
                 Node(self.p5, None, None))
        self.assertEqual(
            delete(T, self.p4, self.cb),
            Node(self.p5, Node(self.p2, Node(self.p1, None, None), Node(self.p3, None, None)), None)
        )

if __name__ == "__main__":
    unittest.main()