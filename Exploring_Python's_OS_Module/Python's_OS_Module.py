import os

def list_directory_contents(path):
    try:
        # Check if the provided path exists and is a directory
        if os.path.exists(path) and os.path.isdir(path):
            print(f"Contents of directory '{path}':")
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                if os.path.isfile(full_path):
                    print(f"File: {item}")
                elif os.path.isdir(full_path):
                    print(f"Directory: {item}")
        else:
            print(f"The path '{path}' does not exist.")
    except PermissionError:
        print("You don't have permission to access this directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt user for directory path
    directory_path = input("Enter the directory path: ")
    list_directory_contents(directory_path)
