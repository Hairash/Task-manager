from app import App
from process_command import process_command

app = App()

print('Go')

cmd = ''

while cmd != 'exit':
    cmd = input()
    process_command(app, cmd)
