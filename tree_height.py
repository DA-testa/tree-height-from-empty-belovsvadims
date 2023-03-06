# python3
# 221RDB129 Vadims Belovs 11.grupa

import sys
import threading
import numpy

def compute_height(n, parents):
    height = numpy.zeros(n)
    def calculate(i):
        if height[i] != 0:
            return height[i]
        if parents[i] == -1:
            height[i] = 1
        else:
            height[i] = calculate([parents[i]]) + 1
        return height[i]

    for i in range(n):
        calculate(i)
    return int(max(height))

    """
    max_height = height[0]
    for i in range(1, n):
        max_height = max(max_height, height[i])

    return max_height
    """


def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision

    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    
    choice = input()
    if choice == "I":
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))
    elif choice == "F":
        fPath = input()
        if 'a' not in fPath:
            with open(str("test/"+fPath), "r") as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
                print(compute_height(n, parents))
        else:
          print("Error")
    else:
      print("Error")
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
