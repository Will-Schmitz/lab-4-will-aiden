import sys 
import unittest 
from typing import * 
from dataclasses import dataclass 
import math, time
from statistics import mean
import matplotlib.pyplot as plt 
import numpy as np 
import random 
from bst import *
sys.setrecursionlimit(10**6) 
 
from bst import * 
 
TREES_PER_RUN : int = 10000 

#Height in edges: empty = -1, leaf = 0. Change if your course uses nodes instead.
def height(BT: BinTree) -> int:
    if BT is None:
     return -1
    return 1 + max(height(BT.left), height(BT.right))

def tree_height_graph_creation(n_max: int, TREES_PER_RUN: int = 10_000) -> None:
    # 50 evenly spaced N from 0..n_max (list first)
    x_coords = [int(n) for n in np.linspace(0, n_max, 50)]
    x_coords = sorted(set(x_coords)) 
    y_coords = [
        mean(height(random_tree(N).tree) for _ in range(TREES_PER_RUN))
        for N in x_coords
    ]

    x_numpy = np.array(x_coords)
    y_numpy = np.array(y_coords)


    plt.plot(x_numpy, y_numpy, label="Average Height")
    plt.xlabel("N (number of nodes)")
    plt.ylabel("Average Tree Height")
    plt.title("Average Tree Height vs N (random BSTs)")
    plt.grid(True)
    plt.legend()
    plt.show()

def random_tree(n: int) -> BinarySearchTree:
    cb = lambda a, b: a < b
    bst = BinarySearchTree(comes_before=cb, tree=None)
    t = bst.tree
    for _ in range(n):
        t = insert(t, random.random(), cb)   # pass cb
    return BinarySearchTree(cb, t)

def time_insert_once(N: int) -> float:
    cb = lambda a, b: a < b
    t = None
    for _ in range(N):
        t = insert(t, random.random(), cb)   # pass cb
    x = random.random()
    t0 = time.perf_counter()
    t = insert(t, x, cb)                      # pass cb
    return time.perf_counter() - t0

def insert_time_graph_creation(n_max: int, TREES_PER_RUN: int = 10_000) -> None:

    x_coords = [int(n) for n in np.linspace(0, n_max, 50)]
    x_coords = sorted(set(x_coords))  

    y_coords = [
        mean(time_insert_once(N) for _ in range(TREES_PER_RUN))
        for N in x_coords
    ]

    x_numpy = np.array(x_coords)
    y_numpy = np.array(y_coords)


    plt.plot(x_numpy, y_numpy, label="Average Insert Time")
    plt.xlabel("N (number of nodes)")
    plt.ylabel("Time to insert one value (s)")
    plt.title("Average Insert Time vs N (random BSTs)")
    plt.grid(True)
    plt.legend()
    plt.show()


if (__name__ == '__main__'): 
    tree_height_graph_creation(15) 
    insert_time_graph_creation(15)