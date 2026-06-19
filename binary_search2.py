def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        # Find the middle element
        mid = (left + right) // 2
        
        # Check if the middle element is our target
        if sorted_list[mid] == target:
            return f"Found {target} at index {mid}!"
        
        # If target is greater, ignore left half
        elif sorted_list[mid] < target:
            left = mid + 1
            
        # If target is smaller, ignore right half
        else:
            right = mid - 1
            
    return f"{target} was not found in the list."

# Let's test it with a sorted list of user IDs
user_ids = [102, 105, 110, 115, 120, 134, 145]
target_id = 120

print("--- RUNNING BINARY SEARCH ---")
result = binary_search(user_ids, target_id)
print(result)
