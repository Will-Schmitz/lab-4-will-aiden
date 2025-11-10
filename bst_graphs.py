import sys
import time
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
import random

from bst import BinarySearchTree, insert, BinTree 
sys.setrecursionlimit(10**6) 
 
from bst import * 
 
TREES_PER_RUN : int = 10000 

# Return the height (in edges) of a binary tree: empty = -1, leaf = 0.
def height(BT: BinTree) -> int:
    if BT is None:
     return -1
    return 1 + max(height(BT.left), height(BT.right))

# Create and show a graph of average tree height versus N using TREES_PER_RUN random BSTs at 50 evenly spaced N values up to n_max.
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

# Build and return a BinarySearchTree of size n filled with random floats in [0,1] using the standard < comparator.
def random_tree(n: int) -> BinarySearchTree:
    cb = lambda a, b: a < b
    bst = BinarySearchTree(comes_before=cb, tree=None)
    t = bst.tree
    for _ in range(n):
        t = insert(t, random.random(), cb)   # pass cb
    return BinarySearchTree(cb, t)

# Build a random BST of size N and measure the elapsed time to insert one additional random value.
def time_insert_once(N: int) -> float:
    cb = lambda a, b: a < b
    t = None
    for _ in range(N):
        t = insert(t, random.random(), cb)   # pass cb
    x = random.random()
    t0 = time.perf_counter()
    t = insert(t, x, cb)                      # pass cb
    return time.perf_counter() - t0

# Create and show a graph of average time to insert one value versus N using TREES_PER_RUN trials at 50 evenly spaced N values up to n_max.
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
    tree_height_graph_creation(12) 
    insert_time_graph_creation(12)