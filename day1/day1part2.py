def calculate_similarity_score(left, right):
    total_score = 0
    
    # Iterate through each number in the left list
    for num in left:
        # Count how many times num appears in the right list
        count_in_right = right.count(num)
        
        # Add num * count_in_right to the total score
        total_score += num * count_in_right
    
    return total_score

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
    
    # Compute the similarity score
    result = calculate_similarity_score(left_list, right_list)
    
    # Output the result
    print(f"Total similarity score: {result}")

