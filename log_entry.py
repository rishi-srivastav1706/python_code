file_name = "log.txt"

with open(file_name, "a") as file:
    file.write("Python program ran successfully.\n")
with open(file_name, "r") as file:
    content = file.read()
    print(content)