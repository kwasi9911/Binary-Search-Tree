# Name: Nana Kwasi Owusu
# Program Description: This program compares the time it takes to search for an item in a list vs searching for it in a binary tree
#Date: June 7, 2024

import random
from BST import *


def populateList(n):
    '''
    This function takes as a parameter a positive integer n
    Returns a list of length n containing a shuffling of the numbers 0 to n - 1
    '''
    listOfItems = list(range(n))
    random.shuffle(listOfItems)
    return listOfItems
    

def searchLength(lst, n):
    '''
    This function takes a list lst and a positive integer n (the value to be searched) as parameters
    The function returns how many elements of lst had to be inspected before finding n.
    If n was not found, it will return the lenghth of lst
    '''
    count = 1
    for i in lst:
        if i ==n:
            return count
        count += 1
    return len(lst)

def listToBST(lst):
    '''
    This function takes a list lst as a parameter and appends its elements to an empty binary search tree in the order provided.
    The function then returns the binary search tree object.
    '''
    tree = BST()
    for i in lst:
        tree.append(i)
    return tree
    
#This is the main part of the program. It compars the performance of lists and BSTs as a function of the number of elements    
if __name__ == "__main__":
    avgComparisonsList = []
    avgComparisonsBST = []

    for n in range(1, 1000, 100):
        sumcountlist = 0
        sumcountbst = 0
        numruns = 0

        for s in range(1, 5):
            lst = populateList(n)
            bst = listToBST(lst)

            for v in range(n):
                sumcountlist += searchLength(lst, v)
                sumcountbst += bst.searchLength(v)
                numruns += 1

        avgComparisonsList.append(sumcountlist / numruns)
        avgComparisonsBST.append(sumcountbst / numruns)

    print(f"Average Search Length for List: {avgComparisonsList}")
    print(f"Average Search Length for BST: {avgComparisonsBST}")
    