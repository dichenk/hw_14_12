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

    def __bool__(self):
        return len(self.content) > 0

    def __len__(self):
        return len(self.content)

##    def __getitem__(self):
##        return f'{self.content} (создано {self.date})'


## зАдАнИе 1
todo_list = set()
todo_list.add(Task('Do homework'))
todo_list.add(Task('Do garden'))
todo_list.add(Task('Do washing'))
todo_list.add(Task('Do homework'))

for i in todo_list:
    print(i)

print()
## ЗАдаНИе 2
todo_list = []
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))

non_empty_tasks = [item for item in todo_list if item]
for i in non_empty_tasks:
    print(i)
print(len([item for item in todo_list if not item]))

print()
## ЗаДаНиЕ 3
class ToDoList:

    def __init__(self, size = 0):
        self.exs = [None] * size

    def __str__(self, item = 'wow'):
        if item != 'wow':
            return str(self.exs[item])
        else:
            a = []
            for i in range(len(self.exs)):
                a.append(str(self.exs[i]))
            return str(a)

    def __setitem__(self, key, value):
        try:
            self.exs[key] = value
        except:
            self.exs.append(value)

    def __getitem__(self, item):
        return self.exs[item]

    def __delitem__(self, item):
        del self.exs[item]

    def __len__(self):
        return len(self.exs)

todo_list = ToDoList()
todo_list[0] = Task('Сдать домашку')
print(todo_list[0])
todo_list[1] = Task('Выпить кофе')
print(todo_list[1])
print('before deliting ', len(todo_list))
print(todo_list)
del todo_list[1]
print('todo_list[0] = ', todo_list[0])
print('after deliting ', len(todo_list))
print('todo_list = ', todo_list)
