import json
import os
import time

# Save tasks in user's home directory for privacy
TASKS_DIR = os.path.expanduser("~/.todo_app")
TASKS_FILE = os.path.join(TASKS_DIR, "tasks.json")

def load_tasks():
    """Load tasks from file if it exists."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("⚠️  Warning: Could not load saved tasks. Starting fresh.")
            return []
    return []

def save_tasks(tasks):
    """Save tasks to file."""
    try:
        # Ensure the directory exists
        os.makedirs(TASKS_DIR, exist_ok=True)
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=2)
    except IOError:
        print("⚠️  Warning: Could not save tasks to file.")

def display_menu():
    """Display the main menu with modern, colorful formatting."""
    print("\n" + "╔" + "═" * 60 + "╗")
    print("║" + " " * 60 + "║")
    print("║" + "           🎯  ADVANCED TO-DO APP MENU" + " " * 16 + "║")
    print("║" + " " * 60 + "║")
    print("╠" + "═" * 60 + "╣")

    # Task Management Section
    print("║  📝 TASK MANAGEMENT" + " " * 39 + "║")
    print("║" + " " * 60 + "║")
    print("║    1. ➕  Add New Task" + " " * 35 + "║")
    print("║    2. 📋  View All Tasks" + " " * 34 + "║")
    print("║    3. ✅  Mark Task Complete" + " " * 30 + "║")
    print("║    4. ✏️   Edit Existing Task" + " " * 29 + "║")
    print("║    5. 🗑️   Delete Task" + " " * 37 + "║")
    print("║" + " " * 60 + "║")
    print("╠" + "═" * 60 + "╣")

    # Analytics & Tools Section
    print("║  📊 ANALYTICS & TOOLS" + " " * 37 + "║")
    print("║" + " " * 60 + "║")
    print("║    6. 📈  View Statistics" + " " * 33 + "║")
    print("║    7. 🔍  Search Tasks" + " " * 36 + "║")
    print("║    8. 🏷️   Filter by Status" + " " * 31 + "║")
    print("║" + " " * 60 + "║")
    print("╠" + "═" * 60 + "╣")

    # System Section
    print("║  ⚙️  SYSTEM" + " " * 47 + "║")
    print("║" + " " * 60 + "║")
    print("║    9. 💾  Save & Backup" + " " * 34 + "║")
    print("║    0. 🚪  Exit Application" + " " * 30 + "║")
    print("║" + " " * 60 + "║")
    print("╚" + "═" * 60 + "╝")

    print("\n💡 Tip: You can also use keyboard shortcuts!")
    print("   Press 'q' for quick add, 'v' for view, 'x' for exit")


def display_tasks(tasks):
    """Display all tasks with better formatting."""
    if not tasks:
        print("\n⚠️  No tasks yet. Let's add one!")
        return
    
    print("\n" + "-" * 50)
    print("             📋 YOUR TASKS")
    print("-" * 50)
    
    pending = []
    completed = []
    
    for i, task_data in enumerate(tasks, 1):
        task = task_data['title']
        status = task_data['completed']
        
        if status:
            completed.append((i, task))
        else:
            pending.append((i, task))
    
    # Display pending tasks
    if pending:
        print("\n🔴 PENDING:")
        for i, task in pending:
            print(f"   {i}. ⬜ {task}")
    
    # Display completed tasks
    if completed:
        print("\n🟢 COMPLETED:")
        for i, task in completed:
            print(f"   {i}. ✅ {task}")
    
    print("-" * 50)


def search_tasks(tasks):
    """Search tasks by keyword."""
    if not tasks:
        print("\n⚠️  No tasks to search!")
        return

    query = input("\n🔍 Enter search term: ").strip().lower()
    if not query:
        print("⚠️  Search term cannot be empty!")
        return

    results = []
    for i, task_data in enumerate(tasks, 1):
        task_title = task_data['title'].lower()
        if query in task_title:
            results.append((i, task_data))

    if results:
        print(f"\n🔍 Found {len(results)} task(s) matching '{query}':")
        print("-" * 50)
        for i, task_data in results:
            status = "✅" if task_data['completed'] else "⬜"
            print(f"   {i}. {status} {task_data['title']}")
        print("-" * 50)
    else:
        print(f"\n❌ No tasks found matching '{query}'")

def filter_tasks(tasks):
    """Filter tasks by completion status."""
    if not tasks:
        print("\n⚠️  No tasks to filter!")
        return

    print("\n🏷️  Filter Options:")
    print("1. Show only pending tasks")
    print("2. Show only completed tasks")
    print("3. Show all tasks")

    choice = input("\n👉 Choose filter (1-3): ").strip()

    if choice == "1":
        filtered = [(i, t) for i, t in enumerate(tasks, 1) if not t['completed']]
        title = "🔴 PENDING TASKS"
    elif choice == "2":
        filtered = [(i, t) for i, t in enumerate(tasks, 1) if t['completed']]
        title = "🟢 COMPLETED TASKS"
    elif choice == "3":
        display_tasks(tasks)
        return
    else:
        print("⚠️  Invalid choice!")
        return

    if filtered:
        print(f"\n{title}:")
        print("-" * 50)
        for i, task_data in filtered:
            status = "✅" if task_data['completed'] else "⬜"
            print(f"   {i}. {status} {task_data['title']}")
        print("-" * 50)
    else:
        print(f"\n❌ No {title.lower()} found!")

def backup_tasks(tasks):
    """Create a backup of current tasks."""
    try:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(TASKS_DIR, f"tasks_backup_{timestamp}.json")

        with open(backup_file, 'w') as f:
            json.dump(tasks, f, indent=2)

        print(f"✅ Backup created: {backup_file}")
        print(f"📊 Total tasks backed up: {len(tasks)}")

    except IOError as e:
        print(f"❌ Backup failed: {e}")

def quick_add_task(tasks):
    """Quick add task without going through full menu."""
    task = input("\n⚡ Quick Add - Enter task: ").strip()
    if task:
        tasks.append({'title': task, 'completed': False})
        print(f"✅ Task added: '{task}'")
        return True
    else:
        print("⚠️  Task cannot be empty!")
        return False


def main():
    tasks = load_tasks()

    print("\n" + "🎉 " * 10)
    print("   Welcome to ADVANCED TO-DO APP! Let's get organized  ")
    print("🎉 " * 10)

    while True:
        display_menu()
        choice = input("\n👉 Choose an option (0-9) or use shortcuts (q/v/x): ").strip().lower()

        # Handle keyboard shortcuts
        if choice == 'q':
            quick_add_task(tasks)
            continue
        elif choice == 'v':
            display_tasks(tasks)
            continue
        elif choice == 'x':
            break

        if choice == "1":
            # Add Task
            task = input("\n✏️  Enter a new task: ").strip()
            if task:
                tasks.append({'title': task, 'completed': False})
                print(f"✅ Task added: '{task}'")
            else:
                print("⚠️  Task cannot be empty!")

        elif choice == "2":
            # View Tasks
            display_tasks(tasks)

        elif choice == "3":
            # Mark Task Complete
            if tasks:
                display_tasks(tasks)
                try:
                    task_num = int(input("\n👉 Enter task number to mark complete: "))
                    if 1 <= task_num <= len(tasks):
                        tasks[task_num - 1]['completed'] = True
                        print(f"✅ Task marked as complete: '{tasks[task_num - 1]['title']}'")
                    else:
                        print("⚠️  Invalid task number")
                except ValueError:
                    print("⚠️  Please enter a valid number")
            else:
                print("\n⚠️  No tasks yet!")

        elif choice == "4":
            # Edit Task
            if tasks:
                display_tasks(tasks)
                try:
                    task_num = int(input("\n👉 Enter task number to edit: "))
                    if 1 <= task_num <= len(tasks):
                        new_task = input("✏️  Enter new task description: ").strip()
                        if new_task:
                            old_task = tasks[task_num - 1]['title']
                            tasks[task_num - 1]['title'] = new_task
                            print(f"✅ Task updated: '{old_task}' → '{new_task}'")
                        else:
                            print("⚠️  Task cannot be empty!")
                    else:
                        print("⚠️  Invalid task number")
                except ValueError:
                    print("⚠️  Please enter a valid number")
            else:
                print("\n⚠️  No tasks yet!")

        elif choice == "5":
            # Remove Task
            if tasks:
                display_tasks(tasks)
                try:
                    task_num = int(input("\n👉 Enter task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"✅ Removed: '{removed['title']}'")
                    else:
                        print("⚠️  Invalid task number")
                except ValueError:
                    print("⚠️  Please enter a valid number")
            else:
                print("\n⚠️  No tasks to remove!")

        elif choice == "6":
            # Show Statistics
            show_statistics(tasks)

        elif choice == "7":
            # Search Tasks
            search_tasks(tasks)

        elif choice == "8":
            # Filter Tasks
            filter_tasks(tasks)

        elif choice == "9":
            # Save & Backup
            save_tasks(tasks)
            backup_tasks(tasks)

        elif choice == "0":
            # Exit
            save_tasks(tasks)
            if tasks:
                pending = sum(1 for t in tasks if not t['completed'])
                print(f"\n👋 Goodbye! You have {pending} pending task(s). See you soon!")
            else:
                print("\n👋 Goodbye! Have a great day!")
            break

        else:
            print("⚠️  Invalid option. Please choose 0-9 or use shortcuts (q/v/x)")

if __name__ == "__main__":
    main()
