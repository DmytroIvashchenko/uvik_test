import datetime
import json

# todo_list = {}

list_of_action = [1, 2, 3, 4, 5]
today = datetime.datetime.today().strftime('%d/%m/%Y')
print('Добрий день!\n'
      'Ви знаходитесь в головному меню to_do_list_app\n')

with open('todo.json', 'r', encoding='utf-8') as read:
    todo_list = json.load(read)


def work_with_json(update):
    file = 'todo.json'
    data = json.dumps(file)
    data = json.loads((str(data)))
    with open(data, 'w', encoding='utf-8') as file:
        json.dump(update, file, indent=4)


def add_action_todo():
    add_action = (input("Яке завдання ви хочете додати до нашого переліку? "))
    todo_list.update({add_action: [None, None]})
    work_with_json(todo_list)
    return todo_list


def del_action_todo():
    del_action = (input("Яке завдання ви хочете видалити з нашого переліку? "))
    todo_list.pop(del_action)
    work_with_json(todo_list)
    return todo_list


def action_selection():
    number_of_action = int(input(
        'Виберіть одну з дій:\n'
        'Додати завдання - 1\n'
        'Видалити завдання - 2\n'
        'Відмитити завдання як виконане - 3\n'
        'Переглянути перелік завдань - 4\n'
        'Переглянути перелік та кількість виконанних завдань - 5\n'
    ))
    return number_of_action


def number_of_tasks_completed():
    accepted_complete = []
    task_progress = list(todo_list.values())
    for task in task_progress:
        if task[0] == 'Complete':
            accepted_complete.append(task)
    return len(accepted_complete)


def accepted_actions():
    accepted = input("Яке завдання виконане? ")
    list_of_actions = list(todo_list.keys())
    i = 0
    while i < len(list_of_actions):
        if accepted == list_of_actions[i]:
            todo_list.update({accepted: ('Complete', today)})
            i += 1
            if i > len(list_of_actions):
                break
        elif accepted != list_of_actions[i]:
            i += 1
            if i > len(list_of_actions):
                break
    work_with_json(todo_list)
    return todo_list


number_of_user_action = action_selection()
while number_of_user_action not in list_of_action:
    once_again = input("Неправильно вибране завдання\nПовторити вибор дії? Y/N ")
    if once_again == 'Y':
        number_of_user_action = action_selection()
    if once_again == 'N':
        print("Гарного дня")
        break

while number_of_user_action == 1 or 2 or 3 or 4 or 5:
    if number_of_user_action == 1:
        add_action_todo()
    if number_of_user_action == 2:
        del_action_todo()
    if number_of_user_action == 3:
        accepted_actions()
    if number_of_user_action == 4:
        print(f'Перелік завдань: {list(todo_list.keys())}')
    if number_of_user_action == 5:
        print(f'{today} виконано {number_of_tasks_completed()} завдання ')
    once_again = input("Виконати ще одну дію? Y/N ")
    if once_again == 'Y':
        number_of_user_action = action_selection()
    if once_again == 'N':
        print("Гарного дня")
        break
