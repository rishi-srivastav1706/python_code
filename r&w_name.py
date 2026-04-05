# 1 & 2: Open "names.txt" in write mode and write 5 names entered by the user
filename = "names.txt"

# Using 'with' automatically closes the file after the block ends
with open(filename, "w") as file:
    print("Enter 5 names:")
    for i in range(5):
        name = input(f"Enter name {i+1}: ")
        # Write each name followed by a newline character
        file.write(name + "\n")

# 3: Open the same file in read mode and print all names
print("\nNames stored in the file:")
with open(filename, "r") as file:
    # Read the entire content of the file and print it
    content = file.read()
    print(content)
