import sys
from utils import render_pages, new_content

def main():
    print("This is argv:", sys.argv)
    command = sys.argv[1]
    print(command)
    if command == "build":
        print("Build was specified - rebuilding site")
        render_pages()
    elif command == "new":
        print("New page was specified - creating new file")
        new_content()
    else:
        print("Please specify ’build’ or ’new’")

main()
