from structure import Node

SPECIAL_SYMBOLS = {
    '^': 'date',
    '=': 'duration',
    '#': 'parent_id'
}

def add_node(string):
    # params of the next node obj
    name = ''
    params = {
        'parent': None,
        'date': None,
        'duration': None,
    }

    words = string.split()
    name_ends = False
    for word in words:
        if word.startswith(tuple(SPECIAL_SYMBOLS.keys())):
            spec_symb = word[0]
            par = word[1:]
            params[SPECIAL_SYMBOLS[spec_symb]] = par
        elif not name_ends:
            name += word + ' '
    # print(name)
    # print(params)
    name = name[:-1]

    return Node(name, params['parent'], params['date'], params['duration'])


test_strings = [
    'Learn English',
    'Try SkyEng ^31.08 =2h #1',
    'Think about papers at school ^01.09 =30m #4',
]

for test_string in test_strings:
    print(add_node(test_string))
