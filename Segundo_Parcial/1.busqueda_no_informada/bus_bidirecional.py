# Function to perform Two Way Linear Search
def search(arr, target):
    # Initialize the starting and ending pointers
    start = 0
    end = len(arr) - 1

    # Iterate till start and end cross each other
    while start <= end:
        # If the start element is equal to target, return
        # start as the index of target element
        if arr[start] == target:
            return start
        # If the ending element is equal to target, return
        # end as the index of target element
        if arr[end] == target:
            return end
        # If target is not equal to starting or ending
        # element, increment start by 1 and decrement end
        # by 1
        start += 1
        end -= 1
    # Return -1 if the target element is not found
    return -1


# Driver code
if __name__ == "__main__":
    # Sample Input
    arr = [3, 9, 12, 16, 20]
    target = 12
    pos = search(arr, target)
    if pos == -1:
        print("Element is not present in array")
    else:
        print(f"Element is present at index {pos}")