"""A small command-line study checklist. Requires Python 3.9 or newer."""

import argparse
import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []
    tasks = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    if not isinstance(tasks, list) or any(
        not isinstance(task, dict)
        or not isinstance(task.get("title"), str)
        or not isinstance(task.get("done"), bool)
        for task in tasks
    ):
        raise ValueError("Invalid task data. Check tasks.json before trying again.")
    return tasks


def save_tasks(tasks):
    temporary = DATA_FILE.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    temporary.replace(DATA_FILE)


def main():
    parser = argparse.ArgumentParser(description="Manage your study checklist.")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="Add a study task")
    add.add_argument("title", help="Put a multi-word title in quotes")
    commands.add_parser("list", help="Show all tasks")
    done = commands.add_parser("done", help="Mark a task as completed")
    done.add_argument("number", type=int, help="Task number shown by list")
    args = parser.parse_args()

    try:
        tasks = load_tasks()
        if args.command == "add":
            title = args.title.strip()
            if not title:
                parser.error("Task title cannot be empty.")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
            print(f"Added task {len(tasks)}: {title}")
        elif args.command == "list":
            if not tasks:
                print('No tasks yet. Try: python main.py add "Learn Git"')
            for number, task in enumerate(tasks, start=1):
                marker = "x" if task["done"] else " "
                print(f"{number}. [{marker}] {task['title']}")
        elif args.command == "done":
            if not 1 <= args.number <= len(tasks):
                parser.error("Task number is out of range. Run list to see your tasks.")
            tasks[args.number - 1]["done"] = True
            save_tasks(tasks)
            print(f"Completed: {tasks[args.number - 1]['title']}")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Error: {error}\n")


if __name__ == "__main__":
    main()
