def display_menu():
    """Display the main menu with better formatting."""
    print("\n" + "=" * 50)
    print("         📝 TO-DO APP MENU")
    print("=" * 50)
    print("1. ➕  Add Task")
    print("2. 📋  View All Tasks")
    print("3. ✅  Mark Task Complete")
    print("4. ✏️   Edit Task")
    print("5. 🗑️   Remove Task")
    print("6. 📊  Show Statistics")
    print("7. 🚪  Exit")
    print("=" * 50)


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


def show_statistics(tasks):
    """Display task statistics."""
    total = len(tasks)
    completed = sum(1 for t in tasks if t['completed'])
    pending = total - completed
    
    print("\n" + "-" * 50)
    print("             📊 STATISTICS")
    print("-" * 50)
    print(f"Total Tasks:     {total}")
    print(f"Completed:       {completed} ✅")
    print(f"Pending:         {pending} ⬜")
    if total > 0:
        percentage = (completed / total) * 100
        print(f"Progress:        {percentage:.1f}%")
    print("-" * 50)


def main():
    tasks = []
    
    print("\n" + "🎉 " * 10)
    print("   Welcome to TO-DO APP! Let's get organized  ")
    print("🎉 " * 10)
    
    while True:
        display_menu()
        choice = input("\n👉 Choose an option (1-7): ").strip()
        
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
            # Exit
            if tasks:
                pending = sum(1 for t in tasks if not t['completed'])
                print(f"\n👋 Goodbye! You have {pending} pending task(s). See you soon!")
            else:
                print("\n👋 Goodbye! Have a great day!")
            break
            
        else:
            print("⚠️  Invalid option. Please choose 1-7")

if __name__ == "__main__":
    main()
