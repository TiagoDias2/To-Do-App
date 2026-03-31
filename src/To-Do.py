def main():
    tasks = []
    
    while True:
        print("\n===== TO-DO MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        print("=====================")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            task = input("Enter a new task: ").strip()
            if task:
                tasks.append(task)
                print(f"✓ Task added: {task}")
            else:
                print("⚠ Task cannot be empty")
                
        elif choice == "2":
            if tasks:
                print("\n--- Your Tasks ---")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("⚠ No tasks yet")
                
        elif choice == "3":
            if tasks:
                print("\n--- Your Tasks ---")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    task_num = int(input("Enter task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"✓ Removed: {removed}")
                    else:
                        print("⚠ Invalid task number")
                except ValueError:
                    print("⚠ Please enter a valid number")
            else:
                print("⚠ No tasks to remove")
                
        elif choice == "4":
            print("Goodbye! 👋")
            break
            
        else:
            print("⚠ Invalid option. Please choose 1-4")

if __name__ == "__main__":
    main()
