import sys
import unittest
from typing import *
from dataclasses import dataclass
from math import sqrt
sys.setrecursionlimit(10**6)

BinTree: TypeAlias = Union[None, "Node"]

@dataclass(frozen=True)
class Node:
    value: Any
    left: BinTree
    right: BinTree

@dataclass(frozen=True)
class BinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    tree: BinTree = None

@dataclass(frozen=True)
class Point2:
    x: float = 0
    y: float = 0
    @property
    def dist(self) -> float:
        return sqrt(self.x**2 + self.y**2)

# Insert a value into the given binary tree using the comparator cb and return the new tree.
def insert(BT: BinTree, val: Any, cb: Callable[[Any, Any], bool]) -> BinTree:
    match BT:
        case None:
            return Node(val, None, None)
        case Node(v, l, r):
            if cb(val, v):
                return Node(v, insert(l, val, cb), r)
            elif cb(v, val):
                return Node(v, l, insert(r, val, cb))
            else:
                return BT

# Return True if the given value is found in the binary tree according to comparator cb, otherwise False.
def lookup(BT: BinTree, val: Any, cb: Callable[[Any, Any], bool]) -> bool:
    match BT:
        case None:
            return False
        case Node(v, l, r):
            if (not cb(val, v)) and (not cb(v, val)):
                return True
            elif cb(val, v):
                return lookup(l, val, cb)
            elif cb(v, val):
                return lookup(r, val, cb)
            else:
                return False 

# Return True if the binary tree is empty (None), otherwise False.
def is_empty(bst: BinTree) -> bool:
    match bst:
        case None:
            return True
        case Node(_, _, _):
            return False

# Delete one occurrence of a value from the binary tree using comparator cb and return the resulting tree.
def delete(BT: BinTree, val: Any, cb: Callable[[Any, Any], bool]) -> BinTree:
    def min_value(n: Node) -> Any:
        while isinstance(n.left, Node):
            n = n.left
        return n.value

    match BT:
        case None:
            return None
        case Node(v, l, r):
            if (not cb(val, v)) and (not cb(v, val)):
                if l is None or r is None:
                    return l or r
                m = min_value(r)          
                return Node(m, l, delete(r, m, cb))
            if cb(val, v):
                return Node(v, delete(l, val, cb), r)
            else:
                return Node(v, l, delete(r, val, cb))
            