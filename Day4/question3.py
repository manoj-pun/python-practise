#Write a function flatten(nested_list) that takes a deeply nested list and returns a single flat list using recursion.


def flatten(nested_list):
    """
    Flattens a deeply nested list into a single flat list using recursion.
    
    Args:
        nested_list: A list that may contain other lists (of any depth)
        
    Returns:
        A flat list containing all non-list elements in order
    """
    result = []
    
    for item in nested_list:
        if isinstance(item, list):
            # Recursive case: item is a list → flatten it and extend result
            result.extend(flatten(item))
        else:
            # Base case: item is not a list → add it directly
            result.append(item)
            
    return result


print(flatten([1, [2, [3, [4, 5]]], 6, [7, [8]]]))