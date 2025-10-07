# Open the file in read mode
with open("text.txt", "r") as file:
    # Read lines into a list
    lines = file.readlines()

    # Count the number of lines
    line_count = len(lines)

# Print the total number of lines
print("Total number of lines:", line_count)
