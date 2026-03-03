#Write a function rotate(lst, k) that rotates a list k positions to the right in-place without using slicing tricks.

def rotate(lst, k):
    n = len(lst)
    if n == 0:
        return
    
    k = k % n  # handle k > n
    
    # Helper function to reverse portion of list
    def reverse(start, end):
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1
    
    # Step 1: Reverse whole list
    reverse(0, n - 1)
    
    # Step 2: Reverse first k elements
    reverse(0, k - 1)
    
    # Step 3: Reverse remaining elements
    reverse(k, n - 1)

nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums)