import matplotlib.pyplot as plt

def read_numbers_from_file(filename):
    """Read numbers from a file and return them as a list of floats."""
    with open(filename, "r") as file:
        return [float(line.strip()) for line in file.readlines()]

# Replace these with the actual file paths
file1 = "auction_average_nodes_7.txt"
file2 = "FCFS_average_nodes_7.txt"

# Read numbers from the files
numbers1 = read_numbers_from_file(file1)
numbers2 = read_numbers_from_file(file2)

# Create a list of timestamps from 0 to 24 (25 timestamps total)
timestamps = list(range(25))

# Plotting the numbers
plt.figure(figsize=(10, 5))  # Set the figure size to ensure visibility of all timestamps
plt.plot(timestamps, numbers1[:25], color='blue', label='Auction Data')
plt.plot(timestamps, numbers2[:25], color='red', label='FCFS Data')

# Adding labels, title, and legend
plt.xlabel('Timestamps')
plt.ylabel('Numbers of Requests')
plt.title('Comparison of Requests for 7 Nodes')
plt.legend()

# Ensure all 25 timestamps are visible on the x-axis
plt.xticks(timestamps)

# Save the plot as a PNG file
plt.savefig('comparison_graph_7.png')

# Show the plot
plt.show()
