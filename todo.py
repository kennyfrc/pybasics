# Init
todo = []

# Read
print("----------")
print("display initialized todo")
def display_todos(todo):
	print(todo)

# Create
print("----------")
print("create task")
def add_todo(todo, task):
	todo.append(task)
	display_todos(todo)

add_todo(todo, "first task")
add_todo(todo, "second task")

# Delete
print("----------")
print("delete task")
def delete_task(todo, index):
	del todo[index]
	display_todos(todo)

delete_task(todo,1)

# Update

print("----------")
print("update task")

def update_task(todo, index, task):
	todo[index] = task
	display_todos(todo)

update_task(todo, 0, "updated task")