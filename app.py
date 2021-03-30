import pandas as pd

from process_command import process_command

DB_FILENAME = 'nodes.csv'


class App:
    def __init__(self):
        # self.db_filename = DB_FILENAME
        self.nodes = pd.read_csv(DB_FILENAME,  index_col=0)

    # process command
    def process_command(self, string):
        process_command(self, string)

    # save nodes to file
    def save_nodes(self):
        self.nodes.to_csv(DB_FILENAME)
