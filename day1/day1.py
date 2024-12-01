def total_distance(left, right):
    # Sort both lists
    left_sorted = sorted(left)
    right_sorted = sorted(right)
    
    # Calculate the total distance
    total_dist = 0
    for l, r in zip(left_sorted, right_sorted):
        total_dist += abs(l - r)
    
    return total_dist

# Function to read input and split the numbers into two lists
def read_input(filename):
    left_list = []
    right_list = []
    
    with open(filename, 'r') as f:
        for line in f:
            # Split the line into two parts and convert to integers
            left_num, right_num = map(int, line.split())
            left_list.append(left_num)
            right_list.append(right_num)
    
    return left_list, right_list

# Main code to execute
if __name__ == "__main__":
    # Read the two lists from the file
    filename = 'input.txt'  # Change this to the path of your input file
    left_list, right_list = read_input(filename)
    
    # Compute the total distance
    result = total_distance(left_list, right_list)
    
    # Output the result
    print(f"Total distance: {result}")

