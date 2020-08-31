# import structure
import add


# import datetime
#
#
# # declare KINDS dict
# class KindsClass:
#     def __init__(self, goal, task):
#         self.goal = goal
#         self.task = task
#
# KINDS = KindsClass('goal', 'task')
#
#
# class Node:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return str([str(el) for el in self.__dict__.values()])
#
#
# class Goal(Node):
#     def __init__(self, name, parent, end_date):
#         super().__init__(name)
#         self.parent = parent
#         self.end_date = end_date
#
#
# class Task(Node):
#     def __init__(self, name, parent, date, duration):
#         super().__init__(name)
#         self.parent = parent
#         self.date = date
#         self.duration = duration
#
#
# def create(name, kind, params):
#     if kind == KINDS.goal:
#         return Goal(name, params['parent'], params['end_date'])
#
#     elif kind == KINDS.task:
#         return Task(name, params['parent'], params['date'], params['duration'])
#
#
# node = create('Learn English', KINDS.goal, {'parent': None, 'end_date': None})
# node2 = create('Try SkyEng', KINDS.task, {
#     'parent': node,
#     'date': datetime.datetime.now().date(),
#     'duration': datetime.timedelta(hours=1)
# })
# print(node)
# print(node2)
