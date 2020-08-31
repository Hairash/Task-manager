from commands import add_cmd, list_cmd, exit_cmd

COMMANDS = {
    'add': add_cmd,
    'exit': exit_cmd,
    'list': list_cmd,
}


def process_command(app, string):
    words = string.split()
    cmd = words[0]
    par = ' '.join(words[1:])
    COMMANDS[cmd](app, par)


# test_strings = [
#     'add Learn English',
#     'add Try SkyEng ^31.08 =2h #1',
#     'add Think about papers at school ^01.09 =30m #4',
# ]
#
# for test_string in test_strings:
#     print(process_command(test_string))
