from node import *

# Symbols used for quick adding task
SPECIAL_SYMBOLS = {
    '^': 'date',
    '=': 'duration',
    '#': 'parent_id'
}


def add_cmd(app, string):
    # params of the next node obj
    name = ''
    params = {
        'parent': None,
        'date': None,
        'duration': None,
    }

    # parse string with special symbols, make params dict from it
    words = string.split()
    name_ends = False
    for word in words:
        if word.startswith(tuple(SPECIAL_SYMBOLS.keys())):
            spec_symb = word[0]
            par = word[1:]
            params[SPECIAL_SYMBOLS[spec_symb]] = par
        elif not name_ends:
            name += word + ' '
    name = name[:-1]

    node_row = create_node_row(name, params['parent_id'], params['date'], params['duration'])
    print('node_row:', node_row)
    app.nodes = app.nodes.append(node_row, ignore_index=True)


def delete_cmd(app, string):
    x = int(string)
    app.nodes = app.nodes.drop([x])


def list_cmd(app, string):
    print(app.nodes)
    # for node in app.nodes:
    #     print(node)


def exit_cmd(app, string):
    exit()


# test_strings = [
#     'Learn English',
#     'Try SkyEng ^31.08 =2h #1',
#     'Think about papers at school ^01.09 =30m #4',
# ]
#
# for test_string in test_strings:
#     print(add_node(test_string))
