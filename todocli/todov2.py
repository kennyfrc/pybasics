class Todo:
	def __init__(self):
		self.todos = []

	def display_todos(self):
		todos = self.todos
		if todos == []:
			print("Your todolist is empty!")
		else:
			i = 0
			for todo in todos:
				print("Task Name: %s | Status: %s" %(todo.task, todo.completed))
				i += 1
		print("------")

	def num_of_tasks(self):
		return len(self.todos)

	def num_of_completed_tasks(self):
		done_tasks = 0
		for todo in self.todos:
			if todo.completed:
				done_tasks += 1
			else:
				continue
		return done_tasks

	def toggle_all(self):
		if self.num_of_tasks() == self.num_of_completed_tasks():
			for todo in self.todos:
				todo.completed = False
		else:
			for todo in self.todos:
				todo.completed = True
		self.display_todos()

	def add_todo(self, task):
		todos = self.todos
		todos.append(Task(task))
		self.display_todos()

	def delete_task(self, index):
		todos = self.todos
		del todos[index]
		self.display_todos()

	def update_task(self, index, task):
		todos = self.todos
		todos[index] = Task(task)
		self.display_todos()

	def toggle_completed(self, index):
		todos = self.todos
		if todos[index].completed == True:
			todos[index].completed = False
		else:
			todos[index].completed = True
		self.display_todos()

class Task:
	def __init__(self, task_name):
		self.task = task_name
		self.completed = False


todo = Todo()
todo.display_todos()
print("Create Task")
todo.add_todo("first task"); todo.add_todo("second task"); todo.add_todo("third task")
print("Delete Task")
todo.delete_task(1)
print("Update Task")
todo.update_task(0, "updated task")
print("Toggle a Task")
todo.toggle_completed(0)
print("Toggle All")
todo.toggle_all()
print("Toggle All Again")
todo.toggle_all()