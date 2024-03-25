from models import Session, Task

class Commands:
    def add(self, args):
        session = Session()

        description = input("Enter task description: ")
        new_task = Task(description=description)
        session.add(new_task)
        session.commit()

        print("Task added successfully.")

        session.close()

    def view(self, args):
        session = Session()

        tasks = session.query(Task).all()
        if not tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for task in tasks:
                print(f"- {task.description}")

        session.close()

    def delete(self, args):
        session = Session()

        task_id = int(input("Enter task ID to delete: "))
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            session.delete(task)
            session.commit()
            print("Task deleted successfully.")
        else:
            print("Task not found.")

        session.close()
