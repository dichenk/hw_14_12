import datetime

class Task:
    def __init__(self, content):
        self.content = content
        self.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return f'{self.content} (создано {self.date})'

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.content == other.content
        return NotImplemented

    def __hash__(self):
        return hash(self.content)

    def __booll__(self):
        return len(self.content) > 0

    def __len__(self):
        return len(self.content)


## задание 1
todo_list = set()
todo_list.add(Task('Do homework'))
todo_list.add(Task('Do garden'))
todo_list.add(Task('Do washing'))
todo_list.add(Task('Do homework'))

for i in todo_list:
    print(i)

## задание 2
todo_list = []
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))

print()
non_empty_tasks = [item for item in todo_list if item]
for i in non_empty_tasks:
    print(i)
print(len([item for item in todo_list if not item]))
