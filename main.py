from utils.logger import *
from App import app

def main():
    clear_log()
    art_ascii()
    print("\033[34mDeveloper By Narngisa\n\033[32mGithub: \033[35mhttps://github.com/Narngisalnw\033[37m")
    print("\nStart ?? [y or n]\n")

    start = input(">> ")
    if start == "y":
        app()
    elif start == "n":
        exit()

if __name__ == "__main__":
    main()