# Minimum Swaps 2
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem
def minimumSwaps(arr):
    # Create a sorted copy of input list
    ref_arr = sorted(arr)
    # Create a map of the values and indexes from input list
    index_dict = {v: i for i,v in enumerate(arr)}
    # Init swap count var
    swaps = 0
    
    # Loop over input list
    for i,v in enumerate(arr):
        # Remember what the correct value should be
        correct_value = ref_arr[i]
        # If the correct value is not at current position, do a swap
        if v != correct_value:
            # Get the index with which to swap
            to_swap_idx = index_dict[correct_value]
            # Swap indexes in both lists
            arr[to_swap_idx], arr[i] = arr[i], arr[to_swap_idx]
            # Update our reference dictionary
            index_dict[v] = to_swap_idx
            index_dict[correct_value] = i
            # Increment our swap count
            swaps += 1
            
    return swaps

arr = [5, 2, 7, 15, 6, 1, 8]
print(minimumSwaps(arr), arr)

arr = [4, 3, 1, 2]
print(minimumSwaps(arr), arr)
