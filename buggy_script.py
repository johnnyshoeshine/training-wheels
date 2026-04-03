import os

def delete_file(filename):
    # Bug: No path validation, potential for path traversal
    os.remove(filename)

def calculate_average(numbers):
    # Bug: ZeroDivisionError if list is empty
    return sum(numbers) / len(numbers)

def greet(name):
    # Bug: String concatenation with potentially None name
    print("Hello, " + name)

if __name__ == "__main__":
    greet(None)
    print(calculate_average([]))
    # delete_file("../sensitive.txt") # dangerous!
