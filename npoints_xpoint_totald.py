# Find all valid points x on the number line,
# such that the SUM of distances from x to each of the n coordinates is less than d.
#
# e.g. coordinates = [1,2,3], d = 2; output = 1 (because only 2 is a valid point x)
# e.g. coordinates = [1,2,3,4,5], d = 10, output = 5 (because 1,2,3,4,5 are all valid)
# e.g. coordinates = [1, 3, 4], d = 5, output = 4 (because 1, 2, 3, 4 are all valid)

# e.g. coordinates = [-4982378], d = 1, output = 3 (itself, itself + 1, itself - 1)
# e.g. coordinates = [3124, 3124, 3124, 3124, 3124, 3124, 3124, 3124, 3124, 3124], d = 0, output = 1

def binary_search_smallest_valid(coordinates, d, low, high):
    while low <= high:
        mid = (low + high) // 2
        total_distance = sum([abs(coord - mid) for coord in coordinates])
        if total_distance <= d:
            high = mid - 1
        else:
            low = mid + 1
    return low

def binary_search_largest_valid(coordinates, d, low, high):
    while low <= high:
        mid = (low + high) // 2
        total_distance = sum([abs(coord - mid) for coord in coordinates])
        if total_distance <= d:
            low = mid + 1
        else:
            high = mid - 1
    return high

def find_valid_area(coordinates, d):
    # Find the lower and upper bounds of valid points usin`g binary search
    lower_bound = binary_search_smallest_valid(coordinates, d, min(coordinates) - d, max(coordinates) + d)
    upper_bound = binary_search_largest_valid(coordinates, d, min(coordinates) - d, max(coordinates) + d)

    # Calculate the total area of valid points
    total_area = max(upper_bound - lower_bound + 1, 0)  # Ensure positive area
    
    print(f"upper: {upper_bound}")
    print(f"lower: {lower_bound}")
    
    return total_area

def main():
    coordinates = [-12341234]
    d = 1
    print(find_valid_area(coordinates, d))

if __name__ == "__main__":
    main()
