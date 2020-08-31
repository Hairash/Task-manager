from process_command import process_command


class App:
    def __init__(self):
        self.nodes = []

    def process_command(self, string):
        process_command(self, string)
