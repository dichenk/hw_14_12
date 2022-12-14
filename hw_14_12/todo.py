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

todo_list = set()
todo_list.add(Task('Do homework'))
todo_list.add(Task('Do garden'))
todo_list.add(Task('Do washing'))
todo_list.add(Task('Do homework'))

for i in todo_list:
    print(i)
