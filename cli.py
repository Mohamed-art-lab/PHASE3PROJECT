from commands import Commands

class CLI:
    def __init__(self):
        self.commands = Commands()

    def run_command(self, args):
        if not args:
            self.print_help()
            return

        command = args[0]
        if command == 'add':
            self.commands.add(args[1:])
        elif command == 'view':
            self.commands.view(args[1:])
        elif command == 'delete':
            self.commands.delete(args[1:])
        else:
            print("Invalid command. Use 'add', 'view', or 'delete'.")

    def print_help(self):
        print("Usage: python main.py [add|view|delete]")
