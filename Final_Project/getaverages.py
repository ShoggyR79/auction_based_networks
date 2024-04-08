def read_numbers_from_file(filename):
    """Read numbers from a file and return them as a list."""
    with open(filename, "r") as file:
        return [float(line.strip()) for line in file if line.strip()]

def write_number_to_file(filename, number):
    """Write a single number to a file."""
    with open(filename, "w") as file:
        file.write(f"{number}\n")

def write_averages_to_file(filename, averages):
    """Write a list of averages to a file."""
    with open(filename, "w") as file:
        for avg in averages:
            file.write(f"{avg}\n")

# Replace these with the actual file paths
file1 = "a1.txt"
file2 = "a2.txt"
file3 = "a3.txt"

# Reading numbers from the files
numbers1 = read_numbers_from_file(file1)
numbers2 = read_numbers_from_file(file2)
numbers3 = read_numbers_from_file(file3)

# Calculating the average of the numbers from all files
averages = [(a + b + c) / 3 for a, b, c in zip(numbers1, numbers2, numbers3)]


# Filename for the output file
output_file = "FCFS_average_nodes_7.txt"

# Writing the average to the output file
write_averages_to_file(output_file, averages)

print(f"Average written to {output_file}")
