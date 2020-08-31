from add import add_node

COMMANDS = {
    'add': add_node,
}


def process_command(string):
    words = string.split()
    cmd = words[0]
    par = ' '.join(words[1:])
    return COMMANDS[cmd](par)


test_strings = [
    'add Learn English',
    'add Try SkyEng ^31.08 =2h #1',
    'add Think about papers at school ^01.09 =30m #4',
]

for test_string in test_strings:
    print(process_command(test_string))