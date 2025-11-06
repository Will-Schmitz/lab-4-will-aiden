import sys 
import unittest 
from typing import * 
from dataclasses import dataclass 
sys.setrecursionlimit(10**6) 

BinTree: TypeAlias = Union[None, "Node"]

@dataclass(frozen = True)
class Node:
    value: Any
    left: BinTree
    right: BinTree

@dataclass(frozen = True)
class BinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    tree: BinTree = None


def insert (BT : BinTree, val : Any) -> BinTree:
    cb = BinarySearchTree.comes_before
    match BT:
        case None:
            return Node(val,None,None)
        case Node(v,l,r):
            if cb(val,v):
                return Node(v,insert(l,val),r)
            elif cb(v,val):
                return Node(v,l,insert(r,val))
            else:
                return BT

def lookup (BT : BinTree, val : Any) -> bool:
    cb = BinarySearchTree.comes_before
    match  BT:
        case None:
            return False
        case Node(v,l,r):
            if v == val:
                return True
            elif cb(val,v):
                return lookup(l,val)
            elif cb(v,val):
                return lookup(r,val)


#Return True iff the BST has no nodes
def is_empty(bst: BinTree) -> bool:
    match bst:
        case None:
            return True
        case Node(_,_):
            return False


BinarySearchTree.comes_before = lambda a, b: a < b
print(10)
class TestBST(unittest.TestCase):
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
        self.assertEqual(lookup(Node(5, Node(3, None, None), Node(7, None, None)), 7), True)

    def test_lookup_false(self):
        self.assertEqual(lookup(Node(5, Node(3, None, None), Node(7, None, None)), 10), False)
if __name__ == "__main__":
    unittest.main()