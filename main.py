import sys
from todo.cli import CLI

def main():
    cli = CLI()
    cli.run_command(sys.argv[1:])

if __name__ == "__main__":
    main()
