import sys
from datetime import date

today = date.today().strftime("%Y-%m-%d")

def print_help_message():
  print('Usage :-')
  print('$ ./todo add \"todo item\"  # Add a new todo')
  print('$ ./todo ls               # Show remaining todos')
  print('$ ./todo del NUMBER       # Delete a todo')
  print('$ ./todo done NUMBER      # Complete a todo')
  print('$ ./todo help             # Show usage')
  print('$ ./todo report           # Statistics')


def add_todo(task):
    f_todo_w.write(f'{task}\n')
    print(f'Added todo: \"{task}\"')

def mark_as_done(index,lines):
    completed = lines[index-1]
    delete_todo_by_index(index,lines)
    f_done_w.write(f'x {today} {completed}')
    print(f'Marked todo #{index} as done.')

def list_todos():
    todos = []
    for line in f_todo_r:
        todos.append(line[:-1])
    if len(todos) == 0:
        print('There are no pending todos!')
        exit()
    todos = list(reversed(todos))
    for index,todo in enumerate(todos):
        print(f'[{len(todos)-index}] {todo}')

def delete_todo_by_index(index,lines):
    del lines[index-1]
    f = open('todo.txt', 'w')
    f.writelines(lines)


if len(sys.argv) == 3:
 arg1 = sys.argv[1]
 arg2 = sys.argv[2]

elif len(sys.argv) == 2:
 arg1 = sys.argv[1]
 arg2 = None

else:
    print_help_message()
    exit()

f_todo_w = open('todo.txt', 'at')
f_done_w = open('done.txt', 'at')
f_todo_r = open('todo.txt', 'rt')
f_done_r = open('done.txt', 'rt')

if arg1 == 'add':
    if not arg2:
        print('Error: Missing todo string. Nothing added!')
        exit()
    add_todo(arg2)

elif arg1 == 'done':
    if not arg2:
        print('Error: Missing NUMBER for marking todo as done.')
        exit()
    index = int(arg2)
    lines = f_todo_r.readlines()
    if index == 0 or index > len(lines) or len(lines) == 0 :
        print(f'Error: todo #{index} does not exist.')
        exit()
    mark_as_done(index,lines)

elif arg1 == 'ls':
    list_todos()

elif arg1 == 'report':
    pending = len(f_todo_r.readlines())
    completed = len(f_done_r.readlines())
    print(f'{today} Pending : {pending} Completed : {completed}')

elif arg1 == 'del':
    if not arg2:
        print('Error: Missing NUMBER for deleting todo.')
        exit()
    index = int(arg2)
    lines = f_todo_r.readlines()
    if index == 0 or index > len(lines) or len(lines) == 0:
        print(f'Error: todo #{index} does not exist. Nothing deleted.')
        exit()
    delete_todo_by_index(index,lines)
    print(f'Deleted todo #{index}')

elif arg1 == 'help':
    print_help_message()