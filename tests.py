from functions.get_file_content import get_file_content
import os



if __name__ == "__main__":
    print("Testing get_file_content function:")
    
    print("\nResult for main.py:")
    print(get_file_content("calculator", "main.py"))
    
    print("\nResult for pkg/calculator.py:")
    print(get_file_content("calculator", "pkg/calculator.py"))
    
    print("\nResult for /bin/cat (should be error):")
    print(get_file_content("calculator", "/bin/cat"))
    
    print("\nResult for pkg/does_not_exist.py (should be error):")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

    print("\nResult for lorem.txt (should be truncated):")
    result = get_file_content("calculator", "lorem.txt")
    print(f"Length: {len(result)} characters")
    print(result[:200] + "..." if len(result) > 200 else result)  # Show first 200 chars