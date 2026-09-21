tasks = []

def add_task():
    task_name = input('Enter a task: ').strip()
    task = {'name': task_name, 'completed': False}
    if task_name != "":
        tasks.append(task)
    else:
        print('Invalid task')
def view_tasks():
    if tasks:
        for number, task in enumerate(tasks, start=1):
            if task['completed']:
                status = '[✓]'
            else:
                status = '[ ]'
            print(number, task['name'], status)
    else:
        print('No tasks available')
def remove_task():
    try:
        remove = int(input('Enter a task number to remove: '))
        tasks.remove(tasks[remove - 1])
        print('task removed successfully')
    except (ValueError, IndexError):
        print('That is not a valid task')
def toggle_tasks():
    try:
        task_number = int(input('Enter a task number: '))
        selected_task = tasks[task_number - 1]
        selected_task['completed'] = not selected_task['completed']
    except (ValueError, IndexError):
        print('That is not a valid task')
while True:
    choices = input('''What would you like to do?
    1. Add a task
    2. View tasks
    3. Remove a task
    4. toggle a task(complete or reverse it)
    5. Exit
    Enter your choice: ''')
    if choices == '1':
        add_task()
    elif choices == '2':
        view_tasks()
    elif choices == '3':
        remove_task()
    elif choices == '4':
        toggle_tasks()
    elif choices == '5':
        break
    else:
        print('Invalid input')