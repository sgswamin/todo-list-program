todo_list = []

while True:

  print("Options:")
  print("1. Add Task")
  print("2. Remove Task")
  print("3. Quit")
  choice = input()
  if choice == "1":
    print("Adding task")
    new_task = input()
    todo_list.append(new_task)
  elif choice == "2":
    if not todo_list:
      print("Your ToDo list is empty")
    else:
      todo_list.pop();
  elif choice == "3":
    print("Quitting")
    break