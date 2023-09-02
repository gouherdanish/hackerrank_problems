"""
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = [int(i) for i in input().strip().split(' ')]
arr = [int(i) for i in input().strip().split(' ')]
A = [int(i) for i in input().strip().split(' ')]
B = [int(i) for i in input().strip().split(' ')]

print(arr)
print(A)
print(B)

# Method 2 - Using list traversal
happiness_idx = 0
for i in range(n):
    if arr[i] in A:
        happiness_idx += 1
    if arr[i] in B:
        happiness_idx -= 1
    
print(happiness_idx)

# Method 1 - Using Set theory
# fails when array has duplicate elems
# intersection_A = set(arr).intersection(A)
# intersection_B = set(arr).intersection(B)

# happiness_idx = len(intersection_A) - len(intersection_B)
# print(happiness_idx)