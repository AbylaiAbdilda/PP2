# ex 1

import os

def list_directories_and_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

def list_all_directories_and_files(path):
    for root, dirs, files in os.walk(path):
        print(f"Directory: {root}")
        print("Files:")
        for file in files:
            print(os.path.join(root, file))
        print()

if __name__ == "__main__":
    path = input()

    print("\n Displaying only directories and files:")
    list_directories_and_files(path)

    print("\n Displaying all directories and files:")
    list_all_directories_and_files(path)
    
# ex 2 

import os

def check(path):
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist")
        return

    if os.access(path, os.R_OK):
        print(f"Path '{path}' is readable")
    else:
        print(f"Path '{path}' is not readable")
    
    
    if os.access(path, os.W_OK):
        print(f"Path '{path}' is writable")
    else:
        print(f"Path '{path}' is not writable")
    

    if os.access(path, os.X_OK):
        print(f"Path '{path}' is executable")
    else:
        print(f"Path '{path}' is not executable")

path_check = "/path/to/your/file_or_directory"
check(path_check)

# ex 3

import os

def analyze(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists")

        dirname = os.path.dirname(path)
        filename = os.path.basename(path)
        print(f"Directory: {dirname}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist")

path = "/path/to/your/file_or_directory"
analyze(path)

# ex 4

def Count(file_path):
    try:
        with open(file_path, "r") as file:
            line_count = 0
            for x in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
        return -1

file_path = "ex_8.py"
num_line = Count(file_path)
if num_line != -1:
    print(f"Number of lines in '{file_path}': {num_line}")

# ex 5

def write_list(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for i in data:
                file.write(str(i) + '\n')
        print("List has been written to the file successfully")
    except IOError:
        print("An error occurred while writing to the file")

if __name__ == "__main__":
    liss = ["apple", "banan", "cherry"]

    file_path = "list.txt"

    write_list(file_path, liss)

# ex 6

import string

def create_files():
    al = string.ascii_uppercase
    for let in al:
        file_name = let + ".txt"
        with open(file_name, 'w') as file:
            file.write("This is file " + file_name)

if __name__ == "__main__":
    create_files()

# ex 7 

def copy_file(s_f, d_f):
    try:
        with open(s_f, 'r') as source:
            with open(d_f, 'w') as destination:
                destination.write(source.read())
        print("File copied successfully")
    except FileNotFoundError:
        print("One of the files does not exist")
    except IOError:
        print("An error occurred while copying the file")

if __name__ == "__main__":
    source_file = input()
    destination_file = input()

    copy_file(source_file, destination_file)

# ex 8 

import os

def del_file(file_path):
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted")
        except PermissionError:
            print(f"You do not have permission to delete '{file_path}'")
        except OSError as e:
            print(f"Error occurred while deleting '{file_path}': {e}")
    else:
        print(f"The file '{file_path}' does not exist")

if __name__ == "__main__":
    file_path = input()
    del_file(file_path)