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

def delete (BT : BinTree, val : Any) -> BinTree:
    
"""
def insert(cb: Callable[[Any, Any], bool], t: BinTree, x: Any) -> BinTree:
    if t is None:
        return Node(x, None, None)
    if cb(x, t.value):
        return Node(t.value, insert(cb, t.left, x), t.right)
    elif cb(t.value, x):
        return Node(t.value, t.left, insert(cb, t.right, x))
    else:
        return t  # equal: keep one copy (no duplicate insert)
"""

#Return True iff the BST has no nodes
def is_empty(bst: BinTree) -> bool:
    match bst:
        case None:
            return True
        case Node(_,_):
            return False

