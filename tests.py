from functions.get_files_info import get_files_info
import os



if __name__ == "__main__":
    print("Result for current directory:")
    print(get_files_info("calculator", "."))

    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))

    print("Result for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))

    print("Result for '../' directory:")
    print(get_files_info("calculator", "../"))