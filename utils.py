from collections import defaultdict, Counter
from itertools import combinations
from functools import lru_cache
import re
import copy

AOC_YEAR = 2023

# reading input
def get_input(day: int, test: bool = False):    
    with open(f"{AOC_YEAR}/input/day{day}{'_test' if test else ''}.txt", "r") as f:
        return f.read()

def get_input_as_rows(day: int, test: bool = False):
    return get_input(day, test).split("\n")

def get_input_as_matrix(day: int, test: bool = False):
    return [list(row) for row in get_input_as_rows(day, test)]

def export_matrix_to_file(m, file_name):
    with open(file_name, 'w') as f:
        for row in m:
            f.write(''.join(row) + '\n')
            
# matrix manupulation
def inbound(m, i, j):
    if i<0 or i >= len(m):
        return False
    if j<0 or j >= len(m[0]):
        return False
    return True

TL, T, TR, R, BR, B, BL, L = (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)

def add_coords(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

def print_matrix(m):
    for row in m:
        to_print = "".join([str(c) for c in row])
        print(to_print)
        
def copy_matrix(m1, m2):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] = m2[i][j]