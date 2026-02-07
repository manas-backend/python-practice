tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Delete task")
    print("4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("✅ Task added!")
    elif choice == "2":
        if not tasks:
            print("❌ No tasks")
        else:
            print("\nYour tasks:")
            for i, t in enumerate(tasks, 1):
                print(i, "-", t)
    elif choice == "3":
        if not tasks:
            print("❌ No tasks to delete")
        else:
            for i, t in enumerate(tasks, 1):
                print(i, "-", t)
            num = int(input("Enter task number: "))
            tasks.pop(num - 1)
            print("🗑️ Task deleted!")
    elif choice == "4":
        print("Bye 👋")
        break
    else:
        print("Invalid choice!")
