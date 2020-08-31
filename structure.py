class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        if parent:
            parent.children.append(self)
        self.children = []

    def __str__(self):
        return str([{key: val} for key, val in self.__dict__.items()])

# TODO: add __del__


class Task(Node):
    def __init__(self, name, parent, date, duration):
        super().__init__(name, parent)
        self.date = date
        self.duration = duration


class Goal(Node):
    def __init__(self, name, parent, end_date):
        super().__init__(name, parent)
        self.end_date = end_date


par = Node('Parent', None)
ch1 = Goal('Child1', par, None)
ch2 = Goal('Child2', par, '30.11')
grch = Task('Grandchild', ch2, '31.08', '2h')

print(par, ch1, ch2, grch, sep = '\n')
