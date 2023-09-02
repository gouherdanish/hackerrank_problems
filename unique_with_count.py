
"""
n = 6
arr = [1 4 4 4 5 3]

counter_dict = {1: 1, 4: 3, 5: 1, 3: 1}
max_count = 3
max_sighted_ids = [4]
"""


def migratoryBirds(arr):
    # Write your code here
    counter_dict = defaultdict(int)
    for elm in arr:
        counter_dict[elm] += 1
    max_count = max(counter_dict.values())
    max_sighted_ids = [k for k,v in counter_dict.items() if v == max_count]
    return min(max_sighted_ids)