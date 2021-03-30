def create_node_row(name, parent_id, date=None, duration=None):
    return dict(name=name, parent=parent_id, date=date, duration=duration)


class Node:
    def __init__(self, name, parent, date=None, duration=None):
        self.name = name
        self.parent = parent
        if parent:
            parent.children.append(self)
        self.children = []
        self.date = date
        self.duration = duration

    def __str__(self):
        return str([{key: val} for key, val in self.__dict__.items()])

# TODO: add __del__


# par = Node('Parent', None)
# ch1 = Node('Child1', par, None)
# ch2 = Node('Child2', par, '30.11')
# grch = Node('Grandchild', ch2, '31.08', '2h')
#
# print(par, ch1, ch2, grch, sep = '\n')
