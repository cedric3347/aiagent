from functions.write_file import write_file
import os



if __name__ == "__main__":
    print("Testing write_file function:")

    print("\nWriting to a file in the root directory(lorem.txt)")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    
    print("\nWriting to a file in a subdirectory(pkg/morelorem.txt)")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    
    print("\nAttempting to write outside the working directory")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
