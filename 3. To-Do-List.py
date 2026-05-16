import json
import os
TODO_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.json")
 
# ============================================================
# 📁 Operating：Add and save to do items
# knowledge points：dictionary、try...except、FileNotFoundError
# ============================================================
 
 
def load_todos():
    """Add and save to do items from file. if file not exist, return empty list."""
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)          # return a list, each item is a dictionary
    except FileNotFoundError:
        # when file not exist, return empty list, and it will be created when save_todos() is called
        return []
    except json.JSONDecodeError:
        # when file damaged (not a valid JSON), reset it to empty list
        print("⚠️  File is corrupted. Resetting to empty list.")
        return []
 
 
def save_todos(todos):
    """Add and save to do items to file"""
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)
 
 
# ============================================================
# ✅ Core Functions: Add, Complete, View
# Knowledge Points: Creation and Access of Dictionary, try...except + ValueError, try...except + IndexError
# ============================================================
 
def add_todo(todos):
    """Add a new to do item."""
    name = input("Please enter the task content: ").strip()
 
    if not name:
        print("❌ Content cannot be empty!  Please try again.")
        return
 
    # Each item is a dictionary，There are two key：
    #   "task"  → task content
    #   "done"  → whether completed
    todo = {
        "task": name,
        "done": False
    }
 
    todos.append(todo)
    save_todos(todos)
    print(f'✅ Added: "{name}"')
 
 
def show_todos(todos):
    """Display all to do items"""
    if not todos:
        print("📋 The list is empty, add some tasks!")
        return
 
    print("\n📋 Your To-Do List:")
    print("-" * 30)
    for i, todo in enumerate(todos):
        # Visualize completion status with emoji: "✅" for done, "⬜" for not done
        status = "✅" if todo["done"] else "⬜"
        print(f"  {i + 1}. {status} {todo['task']}")
    print("-" * 30)
 
 
def complete_todo(todos):
    """Mark a to do item as completed"""
    show_todos(todos)
 
    if not todos:
        return
 
    # --------------------------------------------------------
    # Knowledge Points: try...except + ValueError
    # User might input non-numeric value (e.g., "abc"), int() will raise ValueError
    # --------------------------------------------------------
    try:
        index = int(input("Please enter the task number to complete: ")) - 1
    except ValueError:
        # Catch ValueError：when int() cannot convert the input
        print("❌ Please enter a number!")
        return
 
    # --------------------------------------------------------
    # Knowledge Points: try...except + IndexError（index out of bounds）
    # User might input a number outside the valid range, e.g., only 3 items but input 10
    # --------------------------------------------------------
    try:
        todo = todos[index]
    except IndexError:
        print(f"❌ Item number {index + 1} does not exist. Please select again!")
        return
 
    if todo["done"]:
        print(f'ℹ️  "{todo["task"]}" has already been completed!')
    else:
        # Change the value of the "done" key in the dictionary to True
        todo["done"] = True
        save_todos(todos)
        print(f'🎉 Great! "{todo["task"]}" has been marked as completed!')
 
 
# ============================================================
# 🎮 Main Function: Menu Loop
# Knowledge Points: try...except、pass、KeyboardInterrupt
# ============================================================
 
def main():
    print("=" * 35)
    print("      📝 Python To-Do List")
    print("=" * 35)
 
    # Load existing to do items from file when program starts. If file not exist, it will return an empty list.
    todos = load_todos()
 
    while True:
        print("\nPlease select an action:")
        print("  1. View List")
        print("  2. Add Task")
        print("  3. Complete Task")
        print("  0. Exit Program")
 
        # --------------------------------------------------------
        # Knowledge Points: try...except + pass
        # When user presses Enter or inputs empty content, use pass to skip this iteration
        # --------------------------------------------------------
        try:
            choice = input("\nPlease enter your choice (0-3): ").strip()
        except KeyboardInterrupt:
            # User presses Ctrl+C to exit gracefully, without error
            print("\n\n👋 Goodbye!")
            break
 
        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            add_todo(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "0":
            print("👋 Goodbye! Data has been automatically saved.")
            break
        elif choice == "":
            # User directly presses Enter, do nothing, continue loop
            pass
        else:
            print("❓ Invalid option. Please enter a number between 0 and 3.")
 
 
if __name__ == "__main__":
    main()
 
